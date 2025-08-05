'''
Tema: Ricorsione semplice
Obiettivo: Scrivere una funzione ricorsiva che conti quante volte 
compare un carattere specifico in una stringa.
'''

# Esercizio 05
# Titolo: "Conta quante volte appare una lettera in una stringa"

'''
Traccia:
Implementa la funzione def conta_carattere(s: str, c: str) -> int, 
che restituisce il numero di occorrenze del carattere c nella stringa s.

Vincoli:
Non usare cicli (for, while)

Non usare funzioni built-in come count
Usa solo la ricorsione

Suggerimento:
Controlla il primo carattere di s, poi richiama la funzione sul resto della stringa.
'''

def conta_carattere(s: str, car: str) -> int:

    if s == "":
        return 0
    
    primo = s[0].lower()
    resto = s[1:]
    car = car.lower()

    if primo == car:
        return 1 + conta_carattere(resto, car)
    else:
        return conta_carattere(resto, car)
    
print(conta_carattere(("cuantas C aparecen en esta frase?"), "C"))
