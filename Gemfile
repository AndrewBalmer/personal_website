source "https://rubygems.org"

# Pins all gems to the exact versions GitHub Pages uses — no surprises on deploy.
gem "github-pages", group: :jekyll_plugins
gem "ffi", "~> 1.16.3"

group :jekyll_plugins do
  gem "jekyll-seo-tag"    # <meta> tags, Open Graph, Twitter cards
  gem "jekyll-sitemap"    # auto-generates sitemap.xml
  gem "jekyll-feed"       # auto-generates atom feed
end

# Windows/JRuby performance (safe to leave on macOS/Linux)
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

gem "wdm", "~> 0.1", platforms: %i[mingw x64_mingw mswin]
gem "http_parser.rb", "~> 0.6.0", platforms: %i[jruby]
