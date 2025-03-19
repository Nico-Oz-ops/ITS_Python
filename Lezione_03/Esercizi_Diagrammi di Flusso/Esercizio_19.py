# Esercizio 19 - Calcolo di sequenze condizionali

while True:
    n = input("Inserire un numero intero: ")
    
    # Verifica se l'input è un numero intero
    if n.lstrip("-").isdigit():
        n = int(n)
        break
    else:
        print("Errore. Riprova a inserire un numero intero.")

if n > 0:
    if n % 2 == 0:
        # Se il numero è pari
        cont = 4
        result = 0

        while cont <= n:
            result += cont
            cont += 4 # Incrementa di 4

        print(f"La somma da 1 a {n} che sono divisibili per 4 è: {result}")

    else:
        # Se il numero è dispari
        cont_disp = 1
        result_disp = 1

        while cont_disp <= n:
            result_disp *= cont_disp
            cont_disp += 2 # Incremento di 2

        print(f"Il prodotto dei numeri dispari da 1 a {n} è: {result_disp}")

else:
    print("Errore")