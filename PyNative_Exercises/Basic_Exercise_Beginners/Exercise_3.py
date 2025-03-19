# Exercise 3: Print characters present at an even index number

str = input("Inserire una stringa: ")

# Opzione 1

# for i in range(len(str)):
#     if i % 2 == 0:
#         print(str[i])

# Opzione 2

# length_str = len(str)
# for i in range(0, length_str - 1, 2):
#     print(str[i])

# Opzione 3
# x = list(str)
# for i in x[0::2]:
#     print(i)

# Opzione 4

print(str[0::2])
print(str[::-2])