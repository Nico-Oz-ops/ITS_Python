# Exercise 5: Check if the first and last numbers of a list are the same

# Opzione 1

# numbers_x = [10, 20, 30, 40, 10]
# numbers_y = [75, 65, 35, 75, 30]

# if numbers_x[0] == numbers_x[-1]:
#     print("True")
# else:
#     print("False")

# if numbers_y[0] == numbers_y[-1]:
#     print("True")
# else:
#     print("False")

# Opzione 2

def first_last_number(lista):
    first_num = lista[0]
    last_num = lista[-1]

    if first_num == last_num:
        return True
    else:
        return False

numbers_x = [10, 20, 30, 40, 10]
print(f"Il risultato è: {first_last_number(numbers_x)}")

numbers_y = [75, 65, 35, 75, 30]
print(f"Il risultato è: {first_last_number(numbers_y)}")
