# Best Brownies recipe
# https://www.allrecipes.com/recipe/10549/best-brownies/

# Each ingredient assigned to values of amount needed in original recipe
butter = 1/2
white_sugar = 1
egg = 2
vanilla_ex = 1
cocoa1 = 1/4
cocoa2 = 1
cocoa3 = 1
ap_flour = 1/2
salt = 1/4
baking_pow = 1/2

# Displays the original list of ingredients
print(f"{'=' * 6} Ingredients for Best Brownies {'=' * 6}")

print("\t- 1/2 cup butter")
print("\t- 1 cup white sugar")
print("\t- 2 eggs")
print("\t- 1 teaspoons vanilla extract")
print("\t- 1/4 cup and 1 tablespoon and 1 teaspoons unsweetened cocoa powder")
print("\t- 1/2 cup all-purpose flour")
print("\t- 1/4 teaspoon salt")
print("\t- 1/2 teaspoon baking powder")

print("\n* This yields 16 servings.\n")

recipe_servings = 16

# Prompts user for the number of servings they wish to make
user_servings = int(input("Enter the number of servings you would like to make: "))

# Divides users input of serving size by the original recipes servings
conversion1 = user_servings / recipe_servings

print("\nConversion:")
print(f"{user_servings} / {recipe_servings} "
      f"= {user_servings / recipe_servings} * amount needed for each ingredient\n")

# Multiples the conversion number by the original recipes amounts for each ingredient and displays the conversion
print(f"The recipe for {user_servings} servings is:")
print(f"\t- {butter * conversion1:.2f} cup(s) of butter\n"
      f"\t- {white_sugar * conversion1:.2f} cup(s) white sugar\n"
      f"\t- {egg * conversion1:.2f} egg(s)\n"
      f"\t- {vanilla_ex * conversion1:.2f} teaspoon(s) vanilla extract\n"
      f"\t- {cocoa1 * conversion1:.2f} cup(s) and {cocoa2 * conversion1} tbsp. "
      f"and {cocoa3 * conversion1} tsp. unsweetened cocoa powder\n"
      f"\t- {ap_flour * conversion1:.2f} cup(s) all-purpose flour\n"
      f"\t- {salt * conversion1:.2f} tsp. salt\n"
      f"\t- {baking_pow * conversion1:.2f} teaspoon(s) baking powder")
