'''
Tema: Liste e funzioni built-in
Obiettivo: Ripassare l’uso di all() e delle condizioni booleane.

Nome dell’esercizio: parole_tutte_maiuscole

Traccia:
Scrivi una funzione che, data una lista di parole, 
restituisca solo quelle in cui **tutte le lettere** sono maiuscole.

Esempio:
parole = ["CIAO", "Mondo", "PYTHON", "ok"]  
→ risultato = ["CIAO", "PYTHON"]

Suggerimento: Puoi usare all(c.isupper() for c in parola) per controllare ogni parola.
'''
# Alternativa 1
def parole_tutte_maiuscole(parole: list[str]) -> list[str]:
    return [parola for parola in parole if all(carattere.isupper() for carattere in parola)]

parole = ["CIAO", "Mondo", "PYTHON", "ok"]  
print(parole_tutte_maiuscole(parole))

# Alternativa 2
def parole_tutte_maiuscole(parole: list[str]) -> list[str]:
    risultato = []

    for parola in parole:
        if all(car.isupper() for car in parola):
            risultato.append(parola)
    return risultato

parole = ["CIAO", "Mondo", "PYTHON", "ok"]  
print(parole_tutte_maiuscole(parole))