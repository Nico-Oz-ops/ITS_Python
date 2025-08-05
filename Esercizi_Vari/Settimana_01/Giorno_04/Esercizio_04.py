'''
Tema: Cicli, condizioni, continue
Obiettivo:
Calcolare la somma dei numeri positivi inseriti dall’utente, ignorando quelli negativi. 
Se viene inserito uno 0, il programma lo segnala ma non lo somma. L'inserimento finisce digitando "stop".
'''

# Esercizio 04
# Titolo: "Somma dei positivi"

'''
Traccia:
Crea una funzione somma_positivi() -> None che:

* Chiede all’utente di inserire numeri interi (uno alla volta).
* Termina l’inserimento se l’utente scrive 'stop'.

Se il numero è:

* positivo → lo somma
* negativo → lo ignora
* zero → stampa 'Hai inserito zero, non viene contato.' e lo ignora
* Alla fine stampa la somma totale dei numeri positivi inseriti.

Suggerimento:
* Usa continue per saltare i numeri negativi o lo zero.
* Usa un solo contatore per la somma.
'''

def somma_positivi() -> None:

    somma = 0
    while True:

        num_interi = input("Inserire un numero intero alla volta (oppure digitare 'stop' per terminare): ")

        if num_interi == "stop":
            break

        try:
            valore = int(num_interi)
            if valore > 0:
                somma += valore
            elif valore < 0:
                continue
            else:
                print("Hai inserito zero, non viene contato")

        except ValueError:
            print("Errore, il valore inserito non è un numero intero.")
    
    print(f"La somma totale dei numeri positivi inseriti è: {somma}")

somma_positivi()

