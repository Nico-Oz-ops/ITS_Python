# Ordinal numbers

# Opzione 1

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# for number in numbers:
#     if number == 1:
#         print(f"{number}st")
#     elif number == 2:
#         print(f"{number}nd")
#     elif number == 3:
#         print(f"{number}rd")
#     else:
#         print(f"{number}th")
    
# Opzione 2

numbers = []

for number in range(1, 10):
    numbers.append(number)
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")
              