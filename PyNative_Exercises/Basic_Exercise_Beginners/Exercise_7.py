# Exercise 7: Find the number of occurrences of a substring in a string

# Opzione 1 - uso metodo stringa
str_x = "Emma is good developer. Emma is a writer"

count = str_x.count("Emma")
print(f"Il nome \"Emma\" si trova {count} volte nella stringa")

# Opzione 2 - uso di funzione
def contatore_emma(frase):
    count = 0
    for i in range(len(frase)):
        count += frase[i: i + 4] == "Emma"
    return count

contatore = contatore_emma("Emma is good developer. Emma is a writer")
print(f"il nome di Emma si ripete {contatore} volte nella stringa")
