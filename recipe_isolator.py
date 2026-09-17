from bs4 import BeautifulSoup as bs
import requests, html5lib
import json, time

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}


def newLine():
    """ Prints an empty line in the command line """
    
    print("")
    
    
def clear():
    """ Clears the screen by printing an empty line 100 times """
     
    for _ in range(100):
        print("")



def connect(url, max_retries=5):
    
    """
    GET a URL, retrying with exponential backoff on failure or non-200 status.

    Retries up to max_retries times, sleeping 1s, 2s, 4s, ... between attempts,
    on connection errors (requests.RequestException) or non-200 responses.

    Raises the last exception, or a RuntimeError with the last status code,
    if all retries are exhausted without a 200 response.

    """
    
    
    delay = 1
    last_exc = None
    for attempt in range(max_retries):
        try:
            resp = requests.get(url, headers=HEADERS, timeout=10)
        except requests.RequestException as e:
            last_exc = e
            time.sleep(delay)
            delay *= 2
            continue

        if resp.status_code == 200:
            return resp

        time.sleep(delay)
        delay *= 2

    if last_exc:
        raise last_exc
    raise RuntimeError(f"Failed to fetch {url} after {max_retries} retries, last status {resp.status_code}")

    


def getRecipe(url):
    """
    Fetch a page and extract its embedded Recipe schema.org data.

    Connects to url, parses the HTML, and scans <script type="application/ld+json">
    tags for a JSON-LD object of @type "Recipe" (including one nested inside an
    @graph list). Returns the recipe dict, or None if no Recipe data is found.
    """
       
    
    resp = connect(url)
    print(resp.status_code)
    raw_html = bs(resp.text, "html5lib")
    
    scripts = raw_html.find_all('script', type='application/ld+json')
    
    

    for script in scripts:
        try:
            data = json.loads(script.string)
        except (json.JSONDecodeError, TypeError):
            continue
        
        candidates = data if isinstance(data,list) else data.get("@graph", [data])
            
        for item in candidates:
            item_type = item.get("@type")
            if item_type == "Recipe" or (isinstance(item_type, list) and "Recipe" in item_type):
                return item
        
    return None


def printRecipe(recipe):
    """
    Print a recipe dict's name, ingredients, and instructions to stdout.

    Expects the schema.org Recipe shape: 'name', 'recipeIngredient' (list of
    strings), and 'recipeInstructions' (list of HowToStep and/or HowToSection
    items, the latter printed with its nested steps indented).
    """

        
    print(recipe['name'])

    newLine()
    
    ingredients = recipe['recipeIngredient']
    
    for ingredient in ingredients:
        print(ingredient)
    
    print("")   
    instructions = recipe['recipeInstructions']
    
    newLine()
    for item in instructions:
        
        if item['@type'] == 'HowToStep':
            print(item['text'])
            newLine()
        elif item['@type'] == 'HowToSection':
            print(item['name'])
            newLine()
            for item in item['itemListElement']:
                print(" - " + item['text'])
                newLine()        
              
        
