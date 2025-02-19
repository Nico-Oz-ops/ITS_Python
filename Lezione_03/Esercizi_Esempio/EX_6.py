# Match statement and variables

# Define variables

gender:str = "m"
age:int = 10

# Match statement

match (gender, age):
    case ("f", 5):
        print("Piccola!")
    case ("m", 5):
        print("Piccolo!")
    case ("f", 10):
        print("Grande!")
    case ("m", 10):
        print("Gigante!")
    case _:
        print("Kinder Sorpresa!")