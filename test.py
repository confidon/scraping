import recipe_isolator as isolator
import sys


   
if __name__ == "__main__":

    isolator.clear()
    
    #test_url = "https://www.acozykitchen.com/chunky-monkey-banana-bread"
    test_url = "https://www.allrecipes.com/recipe/223042/chicken-parmesan/" 
    
    recipe = isolator.getRecipe(test_url)
    isolator.printRecipe(recipe)