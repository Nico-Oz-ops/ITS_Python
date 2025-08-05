'''
Tema: Ricorsione su stringhe
Obiettivo: Scrivere una funzione ricorsiva che conti quante volte compare una lettera specifica in una stringa.
'''

# Esercizio 05
# Titolo: "Conta quante volte appare una lettera"

'''
Traccia:
Scrivi una funzione conta_lettera(s: str, lettera: str) -> int che prende una stringa s 
e una singola lettera, e restituisce quante volte quella lettera appare nella stringa s.
Il confronto deve essere case insensitive (cioè 'A' e 'a' sono uguali).

Suggerimento:
Usa s.lower() e lettera.lower() per confrontare senza distinzione tra maiuscole e minuscole

* Caso base: stringa vuota → 0
* Altrimenti controlla la prima lettera e chiama ricorsivamente sulla stringa rimanente
'''

def conta_lettera(stringa: str, lettera: str) -> int:

    if stringa == "":
        return 0
        
    if stringa[0].lower() == lettera.lower():
        return 1 + conta_lettera(stringa[1:], lettera)
    
    else: 
        return conta_lettera(stringa[1:], lettera)

print(conta_lettera("hello world", "o"))















