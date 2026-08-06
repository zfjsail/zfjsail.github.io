#!/usr/bin/env bash

set -euo pipefail

if [[ -n "${RUBY_BIN:-}" ]]; then
  ruby_bin="$RUBY_BIN"
elif [[ "$(uname -s)" == "Darwin" ]] && [[ -x /usr/bin/ruby ]]; then
  # The locked GitHub Pages/Jekyll versions need the macOS Ruby 2.6 runtime.
  ruby_bin=/usr/bin/ruby
else
  ruby_bin="$(command -v ruby)"
fi

bundle_bin="$("$ruby_bin" -e '
  user_bundle = File.join(Gem.user_dir, "bin", "bundle")
  system_bundle = File.join(Gem.bindir, "bundle")
  print File.executable?(user_bundle) ? user_bundle : system_bundle
')"

user_gem_home="$("$ruby_bin" -e 'print Gem.user_dir')"
export GEM_HOME="$user_gem_home"
export PATH="$GEM_HOME/bin:$PATH"

exec "$ruby_bin" "$bundle_bin" exec jekyll liveserve "$@"
