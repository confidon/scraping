from bs4 import BeautifulSoup as bs
import requests, html5lib
import json, time

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}


def connect(url, max_retries=5):
    delay = 1
    for attempt in range(max_retries):
        try:
            resp = requests.get(url, headers=HEADERS, timeout=10)
        except requests.RequestException:
            time.sleep(delay)
            delay *= 2
            continue
        
        if resp.status_code == 200:
            return resp
        
        time.sleep(delay)
        delay *= 2
        
    return resp
    

def newLine():
    print("")
    
    
def clear(): 
    for _ in range(100):
        print("")

def getRecipe(url):
    
    
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


def print_recipe(recipe):
        
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
              
        
