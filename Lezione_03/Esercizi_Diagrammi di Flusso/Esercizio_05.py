# Esercizio 5 - Calcolo della somma dei quadrati fino a un numero intero positivo n


somma = 0
i = 1

while True:
    numero = input("Inserire un numero intero positivo: ")
    
    if numero.isdigit():
        numero = int(numero)
        break
    else:
        print("Errore. Inserire un numero intero")

if numero < 0:
    print("Errore, il numerito inserito deve essere positivo")
else:
    if i < numero:
        for i in range(numero + 1):
            somma += (i**2)
            i += 1
        print(f"La somma dei quadrati fino a {numero} è {somma}")
 


