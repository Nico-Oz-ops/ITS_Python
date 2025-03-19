# Exercise 3: Return multiple values from a function

# Opzione 1
def calculation(a, b):
    somma = a + b
    sottrazione = a - b

    return somma, sottrazione

result = calculation(40, 10)
print(result)

# Opzione 2
# def calculation(a, b):
#     somma = a + b
#     sottrazione = a - b

#     return somma, sottrazione

# somma, sottrazione = calculation(40, 10)

# print(somma)
# print(sottrazione)

# Opzione 3
def calculation(a, b):
    return a + b, a - b

add, sub = calculation(40, 10)
print(add, sub, sep=", ")

