'''
Obiettivo: Allenarti con l’operatore modulo % e le condizioni.
'''

# Esercizio 03
# Titolo: Pari o dispari"

'''
Traccia:
Scrivi una funzione chiamata pari_dispari() che:

Chieda all’utente di inserire un numero intero.

Restituisca:

"Pari" se il numero è divisibile per 2.

"Dispari" altrimenti.
'''

def pari_dispari() -> str:
    while True: 

        try:
            input_num = int(input("Inserire un numero intero: "))
            break

        except ValueError:
            print("Errore, il valore inserito non è un intero")
    
    if input_num % 2 == 0:
        return "Pari"
    else:
        return "Dispari"

print(pari_dispari())