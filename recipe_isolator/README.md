# Recipe Scraper

Extracts recipe data (name, ingredients, instructions) from recipe websites by parsing embedded `schema.org` JSON-LD (`application/ld+json`) data.

## How it works

- `connect(url, max_retries=5)` — GETs a URL with a browser-like User-Agent, retrying with exponential backoff (1s, 2s, 4s, ...) on connection errors or non-200 responses.
- `getRecipe(url)` — fetches the page, parses it with BeautifulSoup/html5lib, and scans `<script type="application/ld+json">` tags for a JSON-LD object of `@type: "Recipe"`.
- `printRecipe(recipe)` — prints the recipe's name, ingredients, and step-by-step instructions to the console.

## Requirements

- Python 3
- `requests`
- `beautifulsoup4`
- `html5lib`

Install with:
```
pip install -r requirements.txt
```

## Usage

Edit the `test_url` in `test.py` to the recipe page you want, then run:
```
python test.py
```

## Notes

Not every site embeds recipe data as JSON-LD, so `getRecipe` may return `None` for some pages.
