'''
Tema: Condizioni e Cicli

Obiettivo: Scrivere una funzione che chiede all’utente una sequenza di numeri interi 
(finché non scrive "stop"), e verifica ogni coppia di numeri consecutivi per vedere 
se almeno uno dei due è pari. Alla fine, stampa quante coppie soddisfano questa condizione.
'''

# Esercizio 01
# Titolo: "Numeri a due a due"

'''
Traccia:
Crea una funzione verifica_coppie() -> None che:

* Chieda all’utente di inserire numeri interi, uno alla volta.
* Termini l’inserimento quando l’utente digita "stop".
* Analizzi le coppie di numeri consecutivi inseriti (es. il primo e il secondo, il secondo e il terzo, ecc.).
* Conti quante coppie hanno almeno un numero pari.
* Stampi il numero totale di coppie trovate e quante tra queste soddisfano la condizione.

Se l’utente inserisce meno di due numeri, stampare: "Non ci sono abbastanza numeri per formare coppie."

Suggerimento:
* Usa una lista per memorizzare i numeri inseriti, poi un ciclo for con range(len(lista) - 1) 
  per scorrere le coppie consecutive.
* Per controllare se un numero è pari: num % 2 == 0.
'''

def verifica_coppie() -> None:

    num_inseriti = []
    cont_pari = 0
    coppie_totale = 0

    while True:
        input_num = input("Inserire numeri interi, uno alla volta (oppure digitare 'stop' per terminare): ")

        if input_num == "stop":
            break

        try:
            valore = int(input_num)
            num_inseriti.append(valore)

        except ValueError:
            print("Errore, il numero inserito non è un intero")

    if len(num_inseriti) < 2:
        print("Non ci sono abbastanza numeri per formare coppie")
        return
    
    for i in range(len(num_inseriti) - 1):
        coppie_totale += 1
        if num_inseriti[i] % 2 == 0 or num_inseriti[i + 1] % 2 == 0:
            cont_pari += 1
            
    print(f"Coppie trovate: {coppie_totale}")
    print(f"Coppie pari: {cont_pari}")

verifica_coppie()


