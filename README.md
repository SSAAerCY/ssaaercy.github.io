# Yuan Chen · Astronomy & Astrochemistry

Source for [Yuan Chen's personal academic website](https://ssaaercy.github.io/), featuring research on interstellar ices, complex organic molecules, and the chemistry of star formation.

## Explore the website

- [About](https://ssaaercy.github.io/) — background, research interests, and selected publications.
- [Research](https://ssaaercy.github.io/research/) — ICEBEAR, JOYS, and CoCCoA, with illustrated summaries of individual studies.
- [Publications](https://ssaaercy.github.io/publications/) — refereed publications, abstracts, and links to papers, DOIs, and ADS records.
- [CV](https://ssaaercy.github.io/cv/) — academic experience, education, teaching, mentoring, and outreach.
- [My story](https://ssaaercy.github.io/cv/story/) — a personal journey into astronomy.

## Built with

The site uses [Jekyll](https://jekyllrb.com/) and [Academic Pages](https://github.com/academicpages/academicpages.github.io), with custom research pages, figure carousels, publication formatting, and light and dark themes. GitHub Actions builds and deploys the site to GitHub Pages.

## Source structure

| Directory | Contents |
| --- | --- |
| `_pages/` | Main pages and CV |
| `_portfolio/` | Research projects and individual study summaries |
| `_publications/` | Publication metadata and abstracts |
| `_data/` | Navigation, project descriptions, figure captions, and citation data |
| `images/` and `files/` | Images and downloadable documents |
| `_includes/`, `_layouts/`, `_sass/`, and `assets/` | Templates, styles, and browser scripts |

## Local development

Use Ruby 3.3 and the Bundler version specified in `Gemfile.lock`:

```sh
bundle config set --local path vendor/bundle
bundle install
bundle exec jekyll serve --host 127.0.0.1 --livereload --strict_front_matter
```

Open [the local preview](http://127.0.0.1:4000/). Production builds and deployment are configured in [the GitHub Pages workflow](.github/workflows/pages.yml).

## Credits

Template provenance is recorded in [UPSTREAM.md](UPSTREAM.md), and its MIT license is retained in [LICENSE](LICENSE). Research figures are credited to their original papers in the figure captions.
