# Scraping

A collection of web scraping tools and scripts.

## Projects

- [`recipe_isolator/`](recipe_isolator/) — extracts recipe data (name, ingredients, instructions) from recipe websites via embedded schema.org JSON-LD data. See its [README](recipe_isolator/README.md) for details.

## Setup

Each project may have its own dependencies — see its individual README. General requirements across this repo include `requests`, `beautifulsoup4`, and `html5lib`.

```
pip install requests beautifulsoup4 html5lib
```
