# Esercizio 15 - Calcolo di intervalli condizionati

while True:
    valore_n = input("Inserire un valore intero: ")
    
    if valore_n.lstrip("-").isdigit():
        valore_n = int(valore_n)
        break
    else:
        print("Errore. Deve inserire un valore intero. Riprova")

if valore_n > 0 and valore_n <= 100:
    somma_pari = 0
    i = 1
    while i <= valore_n:
        if i % 2 == 0:
            somma_pari += i      
        i += 1
    print(f"La somma di tutti i numeri pari compresi tra 1 e {valore_n} è: {somma_pari}")

else:
    if valore_n == 0 or valore_n < 0:
        print("Errore, il valore inserito è 0 o negativo")
    else:
        somma_dispari = 0
        i = 1
        
        while i <= valore_n:
            if i % 2 != 0:
                somma_dispari += i
            i += 1
        print(f"La somma di tutti i numeri dispari compresi tra 1 e {valore_n} è: {somma_dispari}")



