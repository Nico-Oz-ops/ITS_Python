'''
Tema: Ricorsione semplice con stringhe.
Obiettivo: Scrivere una funzione ricorsiva che conti quante vocali ci sono in una stringa.
'''

# Esercizio 03
# Titolo: "Contare vocali"

'''
Traccia:
Scrivi una funzione ricorsiva chiamata count_vocali(s: str) -> int che restituisca il 
numero di vocali (a, e, i, o, u, anche maiuscole) presenti nella stringa s.

Non usare cicli (for, while) né funzioni già pronte come count.

Suggerimento (se ti serve)
Controlla il primo carattere, poi richiama la funzione sul resto della stringa.
'''
def count_vocali(s: str) -> int:
    if s == "":
        return 0
    
    primo = s[0].lower()
    resto = s[1:]

    if primo in "aeiou":
        return 1 + count_vocali(resto)
    else:
        return count_vocali(resto)
print(count_vocali("hola gente coma va"))
print(count_vocali("HolA TodOs"))
print(count_vocali(""))

