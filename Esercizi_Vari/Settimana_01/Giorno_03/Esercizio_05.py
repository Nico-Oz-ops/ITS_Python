'''
Tema: Contare elementi secondo una condizione usando while, input e operatori logici

Obiettivo:
Allenarti a:

* Gestire input multipli in un ciclo while
* Classificare numeri secondo una regola (pari vs dispari)
* Usare due contatori distinti
* Controllare e gestire input non validi
* Ragionare su proprietà numeriche semplici (% 2)
'''

# Esercizio 05
# Titolo: "Quanti pari, quanti dispari"

'''
Traccia:
Scrivi una funzione chiamata conta_pari_dispari() che:

* Chiede all’utente di inserire numeri interi, uno alla volta.
* Termina quando l’utente digita "stop" (insensibile a maiuscole/minuscole).
* Conta quanti numeri pari e quanti dispari sono stati inseriti.
* Ignora i numeri non validi (es. "ciao"), mostrando un messaggio d’errore.

Alla fine stampa:

* Il numero totale di valori validi
* Quanti erano pari
* Quanti erano dispari

Suggerimento:
* Usa try-except per convertire in int.
* Usa due variabili contatore: pari, dispari.
* Un numero è pari se num % 2 == 0, altrimenti è dispari.
* Ricorda di usare .lower() per gestire "stop" in modo flessibile.
'''

def conta_pari_dispari() -> None:

    cont_totale = 0
    cont_pari = 0
    cont_dispari = 0

    while True:
        input_num = input("Inserire un numero intero (oppure digitare 'stop' per terminare): ")

        if input_num.lower() == "stop":
            break

        try:
            valore = int(input_num)
            if valore % 2 == 0:
                cont_pari += 1
            else:
                cont_dispari += 1
            cont_totale += 1
        
        except ValueError:
            print("Errore, il valore inserito non è un numero intero")
    
    print(f"\nNumero totale di valori validi: {cont_totale}")
    print(f"Valor pari: {cont_pari}")
    print(f"Valori dispari: {cont_dispari}")

conta_pari_dispari()


























