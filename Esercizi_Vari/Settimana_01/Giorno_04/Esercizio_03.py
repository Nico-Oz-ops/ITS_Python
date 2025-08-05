'''
Tema: Cicli e condizioni

Obiettivo: Verificare quanti numeri interi inseriti dall’utente 
non rientrano in un intervallo stabilito (ad esempio tra 10 e 100 inclusi).
'''

# Esercizio 03
# Titolo: "Numeri fuori intervallo"

'''
Traccia:
Crea una funzione conta_fuori_intervallo() -> None che:

* Chiede all’utente di inserire numeri interi uno alla volta.
* L’inserimento termina quando l’utente digita "stop".
* Per ogni numero inserito, controlla se non è compreso tra 10 e 100 (inclusi).

Alla fine, stampa:
* Il numero totale di valori inseriti.
* Quanti di questi sono fuori intervallo.
* Quanti sono dentro l’intervallo.

Suggerimento:
* Puoi usare due contatori: uno per i dentro, uno per i fuori.
'''

def conta_fuori_intervallo() -> None:

    cont_totale = 0
    cont_fuori_intervallo = 0
    cont_dentro_intervallo = 0

    while True:
        numeri_interi = input("Inserire un numero intero alla volta (oppure digitare 'stop' per terminare): ")

        if numeri_interi == "stop":
            break

        try:
            valore = int(numeri_interi)
            cont_totale += 1
            if 10 <= valore <= 100:
                cont_dentro_intervallo += 1
            else:
                cont_fuori_intervallo += 1
        
        except ValueError:
            print("Errore, il numero inserito non è un numero intero.")
    
    print(f"Il numero totale di valori inseriti: {cont_totale}")
    print(f"Numeri fuori intervallo '10 - 100': {cont_fuori_intervallo}")
    print(f"Numeri dentro intervallo '10 - 100': {cont_dentro_intervallo}")

conta_fuori_intervallo()