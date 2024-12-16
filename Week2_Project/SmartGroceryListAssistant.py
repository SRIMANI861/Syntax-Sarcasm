smart_grocery_list_assistant_menu_items = ['Add Item to Pantry','View Pantry','Add Recipe','View Recipes','Generate Grocery List','Exit']

pantry_items = []
recipes = {} #we are using dictionary such that the corresponding ingredients will be stored for each recipe.
while True:
    for num,item in enumerate(smart_grocery_list_assistant_menu_items,start=1):
        print(f"{num}. {item}")

    choice = int(input('Enter your choice(1-6): '))
    if(choice == 6):
        print('You are exciting, goodbye!!')
        break
        

########################################1. Adding item to the pantry
    if(choice == 1):
        pantry_item_name = input('Enter pantry item name: ') #user will enter a item
        item_quantity = float(input(f"Enter quantity of {pantry_item_name}: ")) #storing the quantity user entered into a item_quantity
        print(f"Added {item_quantity} of {pantry_item_name} to the pantry.")
        pantry_items.append((pantry_item_name, item_quantity))

########################################2. View the Pantry
    elif(choice == 2):
        if(pantry_items):
            for item_name, quantity in pantry_items:
                print(f"{item_name}: {quantity}")
        else:
            print('Your pantry is empty')

########################################3. Adding a recipe
    elif(choice == 3):
        recipe_name = input('Enter recipe name: ')
        ingredients = [] #we are just storing only the ingredients of the recipe
        while True:
            ingredient_name = input("Enter ingredient name (or 'done' to finish): ")
            if(ingredient_name.lower()=="done"):
                print(f"Recipe {recipe_name} added.")
                recipes[recipe_name] = ingredients # we are using recipes[recipe_name] bcoz, recipe_name will be the key and we are assigning the ingredients list to that particular key(recipe_name)
                break
            ingredient_quantity = float(input(f"Enter quantity of {ingredient_name}: "))
            ingredient_cost = float(input(f"Enter the cost of {ingredient_name}: " ))
            ingredients.append((ingredient_name,ingredient_quantity,ingredient_cost))

########################################4. View Recipes
    elif(choice == 4):
        if(recipes):
            print('Available Recipes: ')
            for recipe_name,ingredients in recipes.items(): #we are looping through the recipes and ingredients in recipes dictionary
                #we are iterating through each item which is recipe and it's corresponding ingredients 
                print(f"Recipe: {recipe_name}")
                for ingredient,quantity,cost in ingredients:
                    print(f" - {ingredient} : {quantity} , ₹{cost}")
        else:
            print('No recipes found')


########################################5. Generating grocery list
    elif(choice == 5):
        if(recipes):
            print('Available recipes: ')
            for recipe_name in recipes.keys():
                print(f'- {recipe_name}')
            
            print('Grocery List with Estimated Costs')

            total_cost = 0
            for ingredient_name,ingredient_quantity,ingredient_cost in ingredients:
                print(f" - **{ingredient_name}** {ingredient_quantity} x {ingredient_cost} = " , f"₹{ingredient_quantity*ingredient_cost}")
                total_cost += ingredient_quantity * ingredient_cost
            print(f'**Total Estimated Cost: ** {total_cost} ')
                



