# Exercise 7: Print the following pattern
n = 5

for i in range(0, n):
    for j in range(n - i, 0, -1):
        print(j, end=" ")
    print()

