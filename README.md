# Yuan Chen 的学术主页

基于 Academic Pages，公开栏目为 **About · Research · Publications · CV**。Gallery 暂时保留在本地，尚未发布。

## 更新内容

以下为主要编辑入口。更详细的个人维护笔记保存在本地 `_docs/维护指南.md`，该目录不上传到 GitHub。

- **换头像/单位/邮箱：**编辑 `_config.yml` 的 `author:`。
- **改自我介绍：**编辑 `_pages/about.md`。
- **改 Research 项目分区：**编辑 `_data/research_projects.yml`；顺序为 ICEBEAR、JOYS、CoCCoA。
- **改 Research 论文卡片及详情：**编辑 `_portfolio/` 中 `kind: paper` 的 `.md` 文件；`project` 指定所属分区。
- **改研究图和图注：**图片在 `images/research/`，图注在 `_data/research_figures.yml`；正文用 `research-figure.html` 插入。
- **加论文：**在 `_publications/` 新增 `.md` 文件；也可用 `scripts/import_publications.py` 导入 BibTeX。
- **论文链接：**Paper 指向出版社网站的 PDF，DOI 指向期刊，ADS 指向文献记录；仅 in press 论文额外显示 arXiv。
- **加相簿照片/绘画：**图片放入 `images/gallery/`，同时在 `_data/gallery.yml` 添加记录。
- **加 PDF：**文件放入 `files/`，在页面正文添加下载链接。
- **更新博士论文：**替换 `files/Yuan_Chen_PhD_thesis.pdf`；About、Academic CV、My story 共用 `_config.yml` 的 `thesis_pdf` 路径。
- **更新 CV：**替换 `files/Yuan_Chen_CV.pdf`；CV 网页文字另在 `_pages/cv.md` 修改。
- **改个人自述：**编辑 `_pages/cv-story.md`；CV 栏目通过 Academic CV / My story 两个入口切换。
- **加会议和 outreach：**在 `_pages/cv.md` 的对应列表中添加日期、活动、地点和参与方式。

## 本地预览

双击 `preview.command`，打开 `http://127.0.0.1:4000/`，并保持终端窗口运行。保存 `.md`、YAML、图片或样式后会自动重新构建并刷新浏览器。修改 `_config.yml` 后需要在终端按 **Control-C**，再重新运行 `preview.command`。

`update-preview.command` 保留为手动构建入口。两个启动文件会优先使用本次配置的临时 Ruby 环境；该环境被清理后，需要按下方步骤配置常规开发环境。

已有 Ruby 3.3 和 Bundler 4.0.16（与 `Gemfile.lock` 一致）时，在本目录执行：

```bash
bundle config set --local path vendor/bundle
bundle install
bundle exec jekyll serve --host 127.0.0.1 --port 4000 --livereload --strict_front_matter
```

只浏览当前已构建版本，可运行：

```bash
python3 -m http.server 4000 --bind 127.0.0.1 --directory _site
```

然后打开 `http://127.0.0.1:4000/`。静态预览不会自动编译 Markdown/YAML 修改。

## GitHub Pages

保存并检查本地预览后，双击 **`publish.command`** 即可上传更新。它会获取远端状态，遵守 `.gitignore`，检查文件大小，并在本地 Ruby 环境可用时构建实际将上传的源码；随后自动创建带时间的提交并推送。无需关闭 `preview.command` 的窗口。

终端显示“源码已上传”后，GitHub Actions 会自动构建和发布。等 [Actions](https://github.com/SSAAerCY/ssaaercy.github.io/actions) 中 build 和 deploy 都成功，再刷新正式网页。没有新修改时不会创建空提交；上次上传失败但已经提交的内容可再次双击重试。若远端有新提交或构建失败，脚本会停止，并保留本地修改，不会强制覆盖 GitHub。

新版源码的目标仓库为 `ssaaercy/ssaaercy.github.io`。上传源码后，在 **Settings → Pages → Source** 选择 **GitHub Actions**。工作流 `.github/workflows/pages.yml` 会在提交到 `main` 或 `master` 后构建并发布。

上传源码时保留 `Gemfile.lock`，不要上传 `_site/`、`.bundle/`、`.venv/` 等缓存或临时环境。详细迁移步骤见维护指南。

`.gitignore` 已排除构建缓存、本地环境、`_docs/`、暂不公开的 Gallery 和未使用的头像备选；主题的 `_includes/`、`_layouts/`、`_sass/`、字体和脚本仍然是网站运行所需的源码，应当保留。正式的 CV、博士论文 PDF、研究图和当前头像会上传。

Gallery 准备好后，在本地取消 `_data/navigation.yml` 最后的导航注释，再从 `_config.yml` 的 `exclude` 和 `.gitignore` 中移除 Gallery 的四个对应条目，重启预览并检查后再提交。`.gitignore` 控制 Git 上传，`_config.yml` 的 `exclude` 控制网页发布，两者作用不同。

## 搜索引擎

首页标题和描述包含 Yuan Chen、陈缘、astronomy 和 astrochemistry；`_includes/profile-schema.html` 将姓名与 ORCID、Google Scholar 联系起来，并标注个人主页与站点名称。`robots.txt` 指向自动生成的 `sitemap.xml`。这些信息帮助搜索引擎识别网站，收录及排名仍由搜索引擎决定。

首次申请收录时，在 Google Search Console 添加 URL 前缀 `https://ssaaercy.github.io/`。选择 HTML 标签验证，把其 `content` 中的验证码写入 `_config.yml` 的 `google_site_verification`，运行 `publish.command` 上传并等待部署后再验证。随后提交 `sitemap.xml`，并在网址检查中对首页请求编入索引。也可把主页地址加到 Google Scholar、ORCID 和机构个人介绍中。

模板来源和版本见 [UPSTREAM.md](UPSTREAM.md)。
