file = open("ESERCIZI_DATA/Lezione_15/example.txt", 'a', )

print(file)

file.close()

'''--------------------'''



# with open("ESERCIZI_DATA/Lezione_15/example.txt", 'a') as file:
    
#     pass

# usando with non è necessario chiudere il file usando nome_file.close(),
# perché Python lo fa automaticamente, in maniera implicita
# l'uso di with è quello più usato

# with open("ESERCIZI_DATA/Lezione_15/example.txt", 'w') as file:
    
#     stringa: str = "Ciao"

#     file.write(stringa)

#     pass


with open("ESERCIZI_DATA/Lezione_15/example.txt", 'r+') as file:

    print(file.read())