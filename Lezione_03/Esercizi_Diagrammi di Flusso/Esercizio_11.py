# Esercizio 11 - Classifica basata su più condizioni

while True:
    n = input("Inserire un valore intero: ")

    if n.lstrip('-').isdigit():
        n = int(n) 
        break
      
    else:
        print("Errore. Devi inserire un numero intero")

if n % 2 == 0 and n > 10:
    print("Numero valido")

else:
    print("Numero non valido")
