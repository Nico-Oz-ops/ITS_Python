'''
Tema: Liste e funzioni any, lambda, filter - rilevamento condizioni multiple

Obiettivo: Verificare se almeno un elemento di una lista soddisfa più condizioni usando any combinato con lambda e filter.

Nome dell’esercizio: Controlla presenza di parole speciali

Traccia:
Scrivi una funzione contiene_parola_speciale(parole: list[str]) -> bool che verifica se almeno una delle parole nella lista:
* Ha più di 5 lettere
* Contiene almeno una cifra numerica

Restituisci True se esiste almeno una parola che soddisfa entrambe le condizioni, altrimenti False.

Esempio:
contiene_parola_speciale(["ciao", "mela123", "pianoforte", "abc"]) ➝ True  
contiene_parola_speciale(["ciao", "cane", "libro", "sedia"]) ➝ False  

Suggerimento: 
Usa any() e filter() per filtrare solo gli elementi che soddisfano entrambe le condizioni.
'''


def contiene_parola_speciale(parole: list[str]) -> bool:
    return any(filter(lambda parola: len(parola) > 5 and any(car.isdigit() for car in parola), parole))

parole_1 = ["ciao", "mela123", "pianoforte", "abc"]
parole_2 = ["ciao", "cane", "libro", "sedia"]

print(contiene_parola_speciale(parole_1))
print(contiene_parola_speciale(parole_2))