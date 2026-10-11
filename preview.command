#!/bin/zsh
# Double-click this file in Finder for automatic builds and browser refreshes.
site_directory="$(cd -- "$(dirname -- "$0")" && pwd)"
cd "$site_directory" || exit 1

temporary_ruby="/private/tmp/yuan-ruby-runtime/run-ruby"
temporary_bundle="/private/tmp/yuan-modern-gems/bin/bundle"
if [[ -x "$temporary_ruby" && -f "$temporary_bundle" ]]; then
  preview_command=("$temporary_ruby" "$temporary_bundle")
elif command -v bundle >/dev/null 2>&1; then
  preview_command=(bundle)
else
  print "A configured Ruby and Bundler environment is required."
  print "See _docs/维护指南.md for local development setup."
  exit 1
fi

if lsof -nP -iTCP:4000 -sTCP:LISTEN >/dev/null 2>&1; then
  print "Port 4000 is already in use."
  print "If the automatic preview is already running, keep using http://127.0.0.1:4000/."
  print "To replace an older preview, press Control-C in its terminal, then run this file again."
  exit 1
fi

print "Open http://127.0.0.1:4000/ in your browser."
print "Saving Markdown, YAML, images, or styles rebuilds the site and refreshes the browser."
print "Keep this terminal open while editing."
print "After changing _config.yml, stop and restart the preview."
print "Press Control-C to stop the preview."
exec "${preview_command[@]}" exec jekyll serve --host 127.0.0.1 --port 4000 --livereload --strict_front_matter
