'''
Tema: Uso del ciclo while con input ripetuto e condizione di uscita

Obiettivo:
Allenarti a:
* Usare il ciclo while per ricevere input multipli da tastiera.
* Continuare ad accettare numeri finché l’utente non scrive una parola chiave.
* Contare quanti numeri sono stati inseriti.
* Gestire input misti (numeri e stringhe) senza far crashare il programma.
'''

# Esercizio 03
# Titolo: "Conta fino a stop"

'''
Traccia:
Scrivi una funzione chiamata conta_fino_a_stop() che:

* Chiede all’utente di inserire numeri uno alla volta.
* Continua a chiedere numeri finché l’utente non scrive "stop" (maiuscole/minuscole non contano).
* Ignora eventuali valori non numerici (es: "ciao"), mostrando un messaggio d’errore.
* Alla fine, stampa quanti numeri validi sono stati inseriti.

Suggerimento:
* Usa un ciclo while True: per continuare a chiedere input.
* Usa .lower() per gestire "stop" in modo insensibile alle maiuscole.
* Usa try-except per gestire gli errori se l’input non è convertibile in int.
'''

def conta_fino_a_stop():

    contatore = 0
    while True:
        input_num = input("Inserire un numero intero (oppure digitare 'stop' per terminare): ")

        if input_num.lower() == "stop":
            break

        try:
            valore = int(input_num)
            contatore += 1 
        
        except ValueError:
            print("Errore, il valore inserito non è un numero intero")
    
    print(f"Sono stati inseriti '{contatore}' numeri validi")

conta_fino_a_stop()


