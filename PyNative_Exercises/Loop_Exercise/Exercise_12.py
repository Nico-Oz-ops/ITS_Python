# Exercise 12 - Visualizza la serie di Fibonacci fino a 10 termini
# Sequenza di Fibonacci: 0 1 1 2 3 5 8 13 21 34 ....

num1 = 0
num2 = 1
print("Sequenza di Finobacci")

# Opzione 1 - Ciclo for
# for num in range(10):
#     print(num1, end=" ")
#     result = num1 + num2
#     num1 = num2
#     num2 = result

# # Opzione 2 - Ciclo while
num = 0
while num < 10:
    print(num1, end=" ")
    result = num1 + num2
    num1 = num2
    num2 = result
    num += 1
