# Exercise 9: Check Palindrome Number

# Opzione 1
# num = input("Inserire un numero: ")

# if num == num[::-1]:
#     print(f"Il numero {num} è un palindromo")
# else:
#     print(f"Il numero {num} non è un palindromo")

# Opzione 2
def palindromo(numero):
    if numero == numero[::-1]:
        return f"Il numero {numero} è un palindromo"
    else:
        return f"Il numero {numero} non è un palindromo"
    
numero = input("Inserire un numero: ")
print(palindromo(numero))

    


