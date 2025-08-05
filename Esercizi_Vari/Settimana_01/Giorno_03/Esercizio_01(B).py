'''
Tema: Filtrare e contare valori con cicli e condizioni

Obiettivo: Contare quanti elementi soddisfano una certa 
condizione usando cicli e logica di controllo.
'''

# Esercizio 01 (B)
# Titolo: "Conta i numeri primi"

'''
Traccia:
Scrivi una funzione chiamata conta_numeri_primi() che:

* Chiede all’utente un numero intero positivo maggiore o uguale a 2.
* Conta quanti numeri primi ci sono da 2 a quel numero (incluso).
* Stampa alla fine il totale dei numeri primi trovati.
'''

def conta_numeri_primi():
    try:
        input_num = int(input("Inserire un numero intero positivo maggiore o uguale a 2: "))
    
    except ValueError:
        print("Errore, il numero inserito non è un intero.")
        return
    
    if input_num < 2:
        print("Errore, il numero inserito deve essere maggiore o uguale a 2.")
        return

    print(f"I numeri primi compresi tra 2 e {input_num} sono:")
    contatore = 0
    for num in range(2, input_num + 1):

        num_primo = True
        for i in range(2, num):
            if num % i == 0:
                num_primo = False
                break

        if num_primo:
            contatore += 1
            print(num)

    print(f"\nIn totale ci sono '{contatore}' numeri primi tra 2 e {input_num}.")

conta_numeri_primi()