import recipe_isolator as isolator
import sys


if __name__ != "__main__":   
    #url  = "https://www.recipetineats.com/chicken-breast-recipe/"
    #url = "https://www.allrecipes.com/recipe/223042/chicken-parmesan/" 
    test_url = sys.argv[-1]
    
    recipe = isolator.getRecipe(test_url)
    instructions = recipe['recipeInstructions']
    
    for ingredient in recipe['recipeIngredient']:
        print(ingredient)
        
    isolator.newLine()
    step = 1
    
    for step in instructions:
        try:
            print(f"{step}. {step['text']}")
        except KeyError:
            pass
        isolator.newLine()
        step += 1
    
    isolator.newLine()
    nutrition_info = recipe['nutrition'] # Dictionary
    
    for value in nutrition_info:
        print(value + ": " + nutrition_info[f'{value}'])
        
if __name__ == "__main__":

    isolator.clear()
    
    #test_url = "https://www.acozykitchen.com/chunky-monkey-banana-bread"
    test_url = "https://www.allrecipes.com/recipe/223042/chicken-parmesan/" 
    
    recipe = isolator.getRecipe(test_url)
    isolator.print_recipe(recipe)