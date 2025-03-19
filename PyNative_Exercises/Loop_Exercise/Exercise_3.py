# Exercise 3: Calculate sum of all numbers from 1 to a given number

# Uso ciclo for
n = int(input("Inserire un numero: "))
somma = 0

for i in range(1, n + 1):
    somma += i
print(somma)

# Uso ciclo while
somma_2 = 0
i = 1

while True:
    
    somma_2 += i
    print(somma_2)

