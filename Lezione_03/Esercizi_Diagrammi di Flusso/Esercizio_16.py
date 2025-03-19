# Esercizio 16 - Filtrare e classificare i numeri

dispari = 0
pari = 0
negativi = 0
positivi = 0
i = 1

while i <= 10:
    while True:
        numero = input(f"Inserire il {i}° numero intero: ")

        if numero.lstrip("-").isdigit():
            numero = int(numero)
            break
        else:
            print("Errore. Inserire un numero intero")

    if numero > 0:
        positivi += 1
        if numero % 2 == 0 and numero > 20:
            pari += 1
        
    else:
        negativi += 1
        if numero % 2 != 0 or numero < -10:
            dispari += 1
    i += 1

print(f"Ci sono {positivi} numeri positivi")
print(f"Ci sono {negativi} numeri negativi")
print(f"Ci sono {pari} numeri positivi pari e maggiori di 20")
print(f"Ci sono {dispari} numeri dispari o minori di -10")