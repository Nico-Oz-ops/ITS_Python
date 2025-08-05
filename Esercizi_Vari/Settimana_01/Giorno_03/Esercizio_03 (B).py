'''
Tema: Uso del ciclo while con accumulatore e condizione di uscita

Obiettivo:
Allenarti a:

* Gestire input multipli dinamici con while
* Usare un accumulatore per sommare valori validi
* Controllare l’input con "stop"
* Ignorare input non validi con try-except

'''

# Esercizio 03(B)
# Titolo: "Somma fino a stop"

'''
Traccia:
Scrivi una funzione chiamata somma_fino_a_stop() che:

* Chiede all’utente numeri interi uno alla volta.
* Termina quando l’utente scrive "stop" (insensibile a maiuscole/minuscole).
* Somma tutti i numeri interi inseriti correttamente.
* Ignora input non validi (es. "ciao"), mostrando un messaggio d’errore.
* Alla fine stampa la somma totale dei numeri inseriti.

Suggerimento:
* Usa un ciclo while True.
* All’inizio del ciclo, controlla se l’input è "stop", prima di tentare int(...).
* Usa una variabile somma = 0 come accumulatore.
* Mostra un messaggio solo se l’input è invalido (es. lettere).
'''

def somma_fino_a_stop():
    somma = 0

    while True:
        input_num = input("Inserire un numero intero alla volta (oppure per terminare inserire 'stop'): ")

        if input_num == "stop":
            break

        try:
            valore = int(input_num)
            somma += valore
        
        except ValueError:
            print("Errore, il valore inserito non è un numero intero")
    
    print(f"La somma totale dei numeri validi inseriti è: {somma}")

somma_fino_a_stop()
