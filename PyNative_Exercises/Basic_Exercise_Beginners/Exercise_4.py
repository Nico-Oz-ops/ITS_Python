# Exercise 4: Remove first n characters from a string

# str = input("Inserire una stringa: ")
# n = int(input("Inserire la quantità di caratteri che vuoi rimuovere: "))

# Opzione 1
# carattere_rimosso = str[n::]
# print(carattere_rimosso)

# Opzione 2

def remove_chars(str, n) -> tuple[str, int]:
    str = input("Inserire una stringa: ")
    n = int(input("Inserire la quantità di caratteri che vuoi rimuovere: "))
    carattere_rimosso = str[n::]
    
    return carattere_rimosso

print(remove_chars("stringa", 2))
print(remove_chars("cola cao", 5))