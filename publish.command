#!/bin/zsh
# Double-click in Finder to validate, commit, and push this website.
setopt ERR_EXIT NO_UNSET PIPE_FAIL

publish_site_directory="${0:A:h}"
publish_temporary_directory=""
publish_lock_directory=""
publish_owns_lock=0
publish_commit_message="${1:-}"

publish_cleanup() {
  local publish_result=$?
  trap - EXIT
  if [[ -n "$publish_temporary_directory" && -d "$publish_temporary_directory" ]]; then
    rm -rf -- "$publish_temporary_directory"
  fi
  if (( publish_owns_lock )); then
    rmdir -- "$publish_lock_directory" 2>/dev/null || true
  fi
  if (( publish_result != 0 )); then
    print -r -- ""
    print -r -- "上传未完成。你的本地文件和已经创建的提交仍然保留。"
  fi
  if [[ -t 0 ]]; then
    print -r -- ""
    print -n -r -- "按 Return 结束。"
    IFS= read -r publish_answer || true
  fi
  exit "$publish_result"
}
trap publish_cleanup EXIT
trap 'exit 130' INT
trap 'exit 143' TERM
trap 'exit 129' HUP

publish_stop() {
  print -u2 -r -- "$1"
  exit 1
}

cd "$publish_site_directory"
command -v git >/dev/null || publish_stop "未找到 Git。请先安装 macOS Command Line Tools。"
publish_git_root="$(git rev-parse --show-toplevel 2>/dev/null)" || publish_stop "此目录还没有连接 Git 仓库。"
[[ "$publish_git_root" == "$publish_site_directory" ]] || publish_stop "请在网站目录中运行这个文件。"
publish_branch="$(git symbolic-ref --quiet --short HEAD)" || publish_stop "当前没有选定分支，请先切回 master。"
[[ "$publish_branch" == master || "$publish_branch" == main ]] || publish_stop "当前分支为 $publish_branch；自动发布仅适用于 master 或 main。"
publish_origin_url="$(git config --get remote.origin.url)" || publish_stop "未配置 origin 仓库。"
case "${publish_origin_url:l}" in
  https://github.com/ssaaercy/ssaaercy.github.io|https://github.com/ssaaercy/ssaaercy.github.io.git|git@github.com:ssaaercy/ssaaercy.github.io|git@github.com:ssaaercy/ssaaercy.github.io.git) ;;
  *) publish_stop "origin 并非你的个人主页仓库，请检查 Git 配置。" ;;
esac

publish_lock_directory="$(git rev-parse --absolute-git-dir)/publish-command.lock"
mkdir -- "$publish_lock_directory" 2>/dev/null || publish_stop "另一个上传窗口可能还在运行。请等它结束后再试。"
publish_owns_lock=1

for publish_git_operation in MERGE_HEAD CHERRY_PICK_HEAD REVERT_HEAD rebase-merge rebase-apply; do
  [[ ! -e "$(git rev-parse --git-path "$publish_git_operation")" ]] || publish_stop "Git 的合并或变基尚未完成，请先解决它。"
done
[[ -z "$(git ls-files --unmerged)" ]] || publish_stop "存在未解决的文件冲突，请先解决它。"

print -r -- "检查 GitHub 上的最新版本…"
git fetch origin
git rev-parse --verify "refs/remotes/origin/$publish_branch" >/dev/null || publish_stop "GitHub 上不存在 $publish_branch 分支。"
git merge-base --is-ancestor "origin/$publish_branch" HEAD || publish_stop "GitHub 上有本地尚未同步的提交。自动上传已停止，请先合并这些修改（可以请 Codex 帮忙）。"

# Ignored files must not have been force-added in a previous Git operation.
[[ -z "$(git ls-files --cached --ignored --exclude-standard)" ]] || publish_stop "有被 .gitignore 排除的文件仍在 Git 中跟踪，请先检查待上传清单。"

while IFS= read -r -d '' publish_file; do
  if [[ -f "$publish_file" && ! -L "$publish_file" ]]; then
    publish_file_bytes="$(stat -f '%z' -- "$publish_file")"
    (( publish_file_bytes <= 104857600 )) || publish_stop "文件超过 GitHub 的 100 MiB 限制：$publish_file。请先压缩或移出网站目录。"
  fi
done < <(git ls-files --cached --others --exclude-standard -z)

git add -A
if ! git diff --cached --quiet; then
  print -r -- ""
  print -r -- "本次更新："
  git diff --cached --stat

  # Describe the change instead of generating an uninformative timestamp.
  while [[ -z "${publish_commit_message//[[:space:]]/}" ]]; do
    [[ -t 0 ]] || publish_stop '请提供具体更新说明，例如：./publish.command "Update teaching experience and CV PDF"'
    print -r -- ""
    print -r -- "请简要描述这次更新，例如：Update teaching experience and CV PDF"
    print -n -r -- "提交说明："
    IFS= read -r publish_commit_message || publish_stop "未输入提交说明，上传已停止。"
  done

  publish_build_command=()
  if [[ -x /private/tmp/yuan-ruby-runtime/run-ruby && -f /private/tmp/yuan-modern-gems/bin/bundle ]]; then
    publish_build_command=(/private/tmp/yuan-ruby-runtime/run-ruby /private/tmp/yuan-modern-gems/bin/bundle)
  elif command -v bundle >/dev/null 2>&1; then
    publish_build_command=(bundle)
  fi
  if (( ${#publish_build_command[@]} )) && ! "${publish_build_command[@]}" check >/dev/null 2>&1; then
    publish_build_command=()
  fi

  if (( ${#publish_build_command[@]} )); then
    print -r -- ""
    print -r -- "检查将要上传的源码能否构建（不会影响正在运行的预览）…"
    publish_temporary_directory="$(mktemp -d "${TMPDIR:-/private/tmp}/yuan-site-publish.XXXXXX")"
    mkdir -- "$publish_temporary_directory/source"
    git checkout-index --all --prefix="$publish_temporary_directory/source/"

    # Resolve a local Bundler path before changing to the staged source snapshot.
    publish_bundle_path_setting="$("${publish_build_command[@]}" config get path --parseable)"
    publish_bundle_path="${publish_bundle_path_setting#path=}"
    if [[ -n "$publish_bundle_path" ]]; then
      [[ "$publish_bundle_path" == /* ]] || publish_bundle_path="$publish_site_directory/$publish_bundle_path"
    fi
    (
      cd "$publish_temporary_directory/source"
      if [[ -n "$publish_bundle_path" ]]; then
        export BUNDLE_PATH="$publish_bundle_path"
      fi
      export BUNDLE_GEMFILE="$publish_temporary_directory/source/Gemfile"
      export JEKYLL_ENV=production
      "${publish_build_command[@]}" exec jekyll build --destination "$publish_temporary_directory/built" --strict_front_matter
    ) || publish_stop "网站构建失败，因此尚未提交或推送。请修正上面的错误后再运行。"
  else
    print -r -- "本地 Jekyll 环境未就绪；本次由 GitHub Actions 检查和构建。"
  fi

  git commit -m "$publish_commit_message"
fi

if [[ "$(git rev-parse HEAD)" == "$(git rev-parse "origin/$publish_branch")" ]]; then
  print -r -- "没有需要上传的修改，本地和 GitHub 已同步。"
  exit 0
fi

print -r -- ""
print -r -- "上传到 GitHub…"
git push --set-upstream origin "$publish_branch"
print -r -- ""
print -r -- "源码已上传！GitHub Actions 接下来会自动构建并发布网页。"
print -r -- "发布进度：https://github.com/SSAAerCY/ssaaercy.github.io/actions"
print -r -- "你的主页：https://ssaaercy.github.io/"
print -r -- "等 build 和 deploy 都显示成功后，再刷新线上网页。"
