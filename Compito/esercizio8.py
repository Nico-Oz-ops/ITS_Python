lista_numeri = []

for numero in range(5): #si itera 5 volte.
    while True: #si ripete finché l'utente non inserisce un numero valido.
        numero = int(input("Inserire un numero intero compreso tra 1 e 30: "))
        if numero >= 1 and numero <= 30:
            lista_numeri.append(numero) #se è valido si aggiunge alla lista_numeri[]
            break
        else:
            print("Per favore, inserire un numero intero compreso tra 1 e 30")

print("\nGrafico a barre")
for numero in lista_numeri:
    print("*" * numero)


