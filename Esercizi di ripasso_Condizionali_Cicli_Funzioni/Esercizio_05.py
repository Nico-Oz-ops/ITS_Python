# Esercizio 5
import math

def hypotenuse(lato_a:float, lato_b:float) -> float:
    hypo = math.sqrt((lato_a) ** 2  + (lato_b) ** 2)

    return hypo

print(hypotenuse(3.0, 4.0))
print(hypotenuse(8.0, 15.0))