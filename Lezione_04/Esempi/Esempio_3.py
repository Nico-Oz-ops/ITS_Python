# 3 - Definire una funzione con nome "subtract"

# Opzione 1
def subtract (a, b):
    sottrazione = a - b
    return sottrazione

print(f"La sottrazione tra 4 e 2 è: {subtract(4, 2)}")
print(f"La sottrazione tra 71 e 69 è: {subtract(71, 69)}")
print(f"La sottrazione tra 675 e 72372 è: {subtract(675, 72372)}")

# Opzione 2
def subtract (a, b):
    sottrazione = a - b
    return sottrazione

print(subtract(int(input("Inserire un numero: ")), (int(input("inserire un numero: ")))))

# Opzione 3
def subtract(a, b):
    
    sottrazione = a - b
    return sottrazione

mysubtract = subtract(4, 1)
print(f"La sottrazione tra 4 e 1 è: {mysubtract}")

