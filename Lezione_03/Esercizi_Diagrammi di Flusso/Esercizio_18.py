# Esercizio 18 - Classifica e somma condizionale

# Opzione 1 - errore
# while True:
#     numero_variabile = input("Inserire un numero intero: ")

#     if numero_variabile.lstrip("-").isdigit():
#         numero_variabile = int(numero_variabile)
#         break
#     else:
#         print("Errore. Inserire un numero intero")
    
# i = 0
# somma = 0
# somma_pari = 0
# somma_dispari = 0

# while i < numero_variabile:
#     while True:
#         valore = input(f"Inserire un {i + 1}° valore intero: ")
#         if valore.lstrip("-").isdigit():
#             valore = int(valore)
#             break
#         else:
#             print("Errore. Inserire un valore intero.")

#     somma += valore
#     media = somma / numero_variabile # qui bisogna dividere per il numero variabile iniziale e non per i, visto che è inizializzato a 0, farà la divisione per numero_valido - 1

#     if valore % 2 == 0 and valore > media:
#         somma_pari += valore

#     else:
#         if valore % 2 != 0 or valore < media:
#             somma_dispari += valore

#     i += 1

# print(f"La somma dei numeri pari e maggiori della media è: {somma_pari}.")
# print(f"La somma dei numeri dispari o minori della media è: {somma_dispari}.")
# print(f"La media è: {media:.2f}")

# if somma_pari > somma_dispari:
#     print("La somma dei numeri pari e maggiori della media è maggiore.")

# elif somma_dispari > somma_pari:
#     print("La somma dei numeri dispari o minori della media è maggiore.")

# else:
#     print("Le somme dei numeri pari e dispari sono uguali.")



# Opzione 2

while True:
    numero_variabile = input("Inserire un numero intero: ")

    if numero_variabile.lstrip("-").isdigit():
        numero_variabile = int(numero_variabile)
        break
    else:
        print("Errore. Inserire un numero intero")
    
i = 0
somma = 0
somma_pari = 0
somma_dispari = 0
valori = []

while i < numero_variabile:
    while True:
        valore = input(f"Inserire un {i + 1}° valore intero: ")
        if valore.lstrip("-").isdigit():
            valore = int(valore)
            valori.append(valore)
            somma += valore
            break
        else:
            print("Errore. Inserire un valore intero.")

    i += 1

media = somma / i 

for valore in valori:
    if valore % 2 == 0 and valore > media:
        somma_pari += valore

    else:
        if valore % 2 != 0 or valore < media:
            somma_dispari += valore

print("-" * 50)
print(f"La somma dei numeri pari e maggiori della media è: {somma_pari}.")
print(f"La somma dei numeri dispari o minori della media è: {somma_dispari}.")
print(f"La media è: {media:.2f}")

if somma_pari > somma_dispari:
    print("La somma dei numeri pari e maggiori della media è maggiore.")

elif somma_dispari > somma_pari:
    print("La somma dei numeri dispari o minori della media è maggiore.")

else:
    print("Le somme dei numeri pari e dispari sono uguali.")

