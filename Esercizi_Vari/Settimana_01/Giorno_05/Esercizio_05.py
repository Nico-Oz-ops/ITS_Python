'''
Tema: Cicli, numeri, condizioni, contatori
Obiettivo: Chiedere all’utente di inserire numeri interi fino a quando scrive "fine", 
e alla fine stampare quanti erano pari, dispari e quanti erano zeri.
'''

# Esercizio 04
# Titolo: "Pari, dispari o zero"

'''
Traccia:
Scrivi una funzione conta_pari_dispari_zero() -> None che:

* Chieda all’utente di inserire numeri interi uno alla volta.
* Il ciclo continua fino a che l’utente scrive "fine".

Per ogni numero:

* Se è zero, conta quanti zero sono stati inseriti.
* Se è pari diverso da zero, incrementa un contatore dei pari.
* Se è dispari, incrementa un contatore dei dispari.
* Alla fine, stampa i tre totali.

Suggerimento:
Puoi usare .strip().lower() per pulire l’input, 
e un blocco try/except per evitare crash se l’utente non inserisce numeri validi.
'''

def conta_pari_dispari_zero() -> None:
    count_pari = 0
    count_dispari = 0
    count_zero = 0

    while True:
        input_num = input("Inserire un numero intero (oppure digitare 'fine' per terminare): ").strip().lower()

        if input_num == "fine":
            break

        try:
            valore = int(input_num)

            if valore == 0:
                count_zero += 1
            
            elif valore % 2 == 0:
                count_pari += 1
            
            else:
                count_dispari += 1
        
        except ValueError:
            print("Errore, il valore inserito non è un numero intero.")
    
    print(f"Numero di volte di zero inserito: {count_zero}")
    print(f"Numero di volte di numeri pari inseriti: {count_pari}")
    print(f"Numero di volte di numeri dispari inseriti: {count_dispari}")

conta_pari_dispari_zero()














