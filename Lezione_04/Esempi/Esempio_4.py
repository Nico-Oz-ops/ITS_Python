# 4 - Definire una funxzione che ritorni multipli valori (ritorna una tupla)

def operations(a, b) -> tuple[int, int]:
    sum_result = a + b
    diff_result = a - b

    # Returns a tuple with two values
    return sum_result, diff_result

# Assigns values to two variables
sum_value, diff_value = operations(15, 25)
# print(f"Somma: {sum_value}")
# print(f"Sottrazzione: {diff_value}")

sum_value_2, diff_value_2 = operations(int(input("Insertar un numero intero: ")), int(input("Insertar un numero intero: ")))
print(f"Somma: {sum_value_2}")
print(f"Sottrazzione: {diff_value_2}")


