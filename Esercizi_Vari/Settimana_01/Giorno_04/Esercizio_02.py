'''
Tema: Cicli e Stringhe

Obiettivo:
Scrivere una funzione che riceva in input una frase e conti quante 
vocali e quante consonanti contiene (ignorando spazi, numeri e punteggiatura).
'''

# Esercizio 02
# Titolo: "Conta vocali e consonanti"

'''
Traccia:
Crea una funzione conta_lettere() -> None che:

* Chiede all’utente una frase tramite input().
* Analizza solo i caratteri alfabetici (isalpha()).
* Conta quante vocali (a, e, i, o, u) ci sono.
* Conta quante consonanti ci sono.
* Ignora spazi, numeri, simboli e punteggiatura.

Alla fine stampa:

* Numero totale di vocali
* Numero totale di consonanti

Suggerimento:

* Usa char.lower() per gestire lettere maiuscole.
* Puoi usare un set
'''

def conta_lettere() -> None:
    frase = input("Inserire una frase: ")

    cont_vocali = 0
    cont_consonanti = 0

    vocali = {"a", "e", "i", "o", "u"}

    for car in frase:
        if car.isalpha():
            if car.lower() in vocali:
                cont_vocali += 1
            else:
                cont_consonanti += 1
    
    print(f"La frase '{frase}' ha: \n{cont_vocali} vocali\n{cont_consonanti} consonanti")

conta_lettere()
