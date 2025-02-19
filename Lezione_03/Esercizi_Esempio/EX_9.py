# Match Statement and tuples

# Define a tuple

point = (12, 10)

# Match statement
match point:

    case (0, 0):
        print("Origine")

    case (x, 0):
        print(f"Punto sull'asse X: ({x}, 0)")
    
    case (0, y):
        print(f"Punto sull'asse Y: (0, {point[1]})")
    
    case (x, y):
        print(f"Punto generico: ({x}, {y})")