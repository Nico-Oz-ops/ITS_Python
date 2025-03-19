# Exercise 11: Stampa tutti i numeri primi all'interno di un intervallo

start = 25
end = 50

print(f"I numeri primo tra {start} e {end} sono: ")

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(f"{num}")



