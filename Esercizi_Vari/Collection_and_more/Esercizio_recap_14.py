'''
Tema: Liste e funzioni built-in
Obiettivo: Ripassare l’uso di any() per verificare condizioni sui caratteri.

Nome dell’esercizio: parole_con_numero

Traccia:
Scrivi una funzione che, data una lista di parole, restituisca solo quelle che contengono almeno un numero.

Esempio:
parole = ["casa", "a1b", "python3", "ciao"]  
→ risultato = ["a1b", "python3"]

Suggerimento: Puoi usare any(car.isdigit() for car in parola) per controllare ogni parola.
'''

def parole_con_numero(parole: list[str]) -> list[str]:
    return [parola for parola in parole if any(carattere.isdigit() for carattere in parola)]

parole = ["casa", "a1b", "python3", "ciao"]  
print(parole_con_numero(parole))