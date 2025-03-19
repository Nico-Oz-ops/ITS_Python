numeri = []
somma_pari = 0
somma_dispari = 0
count_dispari = 0

while True:
    num = int(input("Inserire un numero intero (digitare 0 per terminare): "))
    if num == 0: #se l'utente digita 0 il ciclo termina.
        break
    numeri.append(num) #si aggiungono i numeri interi (num) alla lista numeri[]

for num in numeri: #scorre ogni numero (num) della lista (numeri).
    if num % 2 == 0: #se i numeri (num) sono pari li somma.
        somma_pari += num
    elif num % 2 != 0: #se i numeri (num) sono dispari li somma e li conta.
        somma_dispari += num
        count_dispari += 1

media_dispari = somma_dispari / count_dispari if count_dispari > 0 else 0 #calcolo della media solo se ci sono numeri dispari, altrimenti 0.

print(f"La somma dei numeri pari è: {somma_pari}")
print(f"La media dei numeri dispari è: {media_dispari:.2f}")

# "----------------------------------------------------------"

# dizionario_frequenze = {}

# while True:
#     numero_inserito = int(input("Inserisci il numero: "))

#     if numero_inserito in dizionario_frequenze:
#         dizionario_frequenze[numero_inserito] += 1
#     else:
#         dizionario_frequenze[numero_inserito] = 1
