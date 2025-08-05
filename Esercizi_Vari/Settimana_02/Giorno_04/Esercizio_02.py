'''
Tema: Ricorsione su stringhe
Obiettivo: Restituire la stringa in input senza vocali, usando ricorsione.
'''

# Esercizio 02
# Titolo: "Rimuovi vocali"

'''
Traccia:
Scrivi una funzione ricorsiva rimuovi_vocali(s: str) -> str che prende una stringa 
e restituisce una nuova stringa senza le vocali (a, e, i, o, u - sia maiuscole che minuscole).
'''

def rimuovi_vocali(s: str) -> str:
    if s == "":
        return ""
    
    car = s[0].lower()

    if car not in "aeiou":
        return car + rimuovi_vocali(s[1:])
    
    else:
        return rimuovi_vocali(s[1:])

print(rimuovi_vocali("Hola mundo"))