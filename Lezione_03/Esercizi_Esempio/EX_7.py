# Match statement and list

# Define a list
ingredients = ["paSTA", "poMOdoro", "BAsIlico", "mozzaRella"]
ingredients = [ingredients.lower() for ingredients in ingredients]

# Match statement

match ingredients:
    case ["pomodoro", "mozzarella", "basilico"]:
        print("Puoi fare una Caprese!")

    case ["pasta", "pomodoro", *_]:
        print("Puoi fare una Pasta al Pomodoro!")

    case ["pane", "prosciutto", "formaggio"]:
        print("Puoi fare un Panino!")
    
    case _:
        print("Non so cosa fare con questi ingredienti!")
# In this example, the match statement is used to match the value of the variable ingredients.
# The match statement is followed by a series of case statements, each of which specifies a possible value of ingredients.
# The case statement can also contain a list of values, which is matched against the value of ingredients.
# The * operator is used to match the rest of the list.


