#!/bin/zsh
# Rebuild Markdown/YAML sources before refreshing the static preview.
site_directory="$(cd -- "$(dirname -- "$0")" && pwd)"
cd "$site_directory" || exit 1

temporary_ruby="/private/tmp/yuan-ruby-runtime/run-ruby"
temporary_bundle="/private/tmp/yuan-modern-gems/bin/bundle"
if [[ -x "$temporary_ruby" && -f "$temporary_bundle" ]]; then
  build_command=("$temporary_ruby" "$temporary_bundle")
elif command -v bundle >/dev/null 2>&1; then
  build_command=(bundle)
else
  print "A configured Ruby and Bundler environment is required."
  print "See _docs/维护指南.md for local development setup."
  exit 1
fi

print "Building the website…"
if "${build_command[@]}" exec jekyll build --strict_front_matter; then
  print "Updated successfully. Refresh http://127.0.0.1:4000/ with Command-R."
  print "If the preview is not running, double-click preview.command first."
else
  print "Build failed. Fix the error above, then run this file again."
  exit 1
fi
