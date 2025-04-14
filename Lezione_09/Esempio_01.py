from typing import Callable

# Esempio 1
square:Callable[[int], int] = lambda x: x ** 2
print(square(5))

# Esempio 2
multiply:Callable[[float, float], float] = lambda a, b: a * b
print(multiply(3, 4.5))

# Esempio 3
multiply:Callable[[float, float, float], float] = lambda a, b, c: a * b * c
print(multiply(3.35, 0.4, 2.5))

# Esempio 4
