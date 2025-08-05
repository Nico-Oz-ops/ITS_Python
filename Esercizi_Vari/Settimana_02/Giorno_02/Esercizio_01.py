'''
Tema: Ricorsione semplice
Obiettivo: Scrivere una funzione ricorsiva che, data una stringa, 
verifichi se è palindroma (si legge uguale da sinistra a destra e da destra a sinistra).
'''

# Esercizio 01
# Titolo: "Verifica se una stringa è palindroma (ricorsione)"

'''
Traccia:
Implementa la funzione is_palindroma(s: str) -> bool che restituisce True se la stringa s è palindroma, altrimenti False.

Vincoli:
* Usa solo la ricorsione
* Non usare cicli (for, while)
* Evita funzioni o slicing con passo negativo ([::-1])
* È permesso usare l’accesso diretto a caratteri con indici

Suggerimento:
* Controlla se il primo e l’ultimo carattere sono uguali.
* Richiama la funzione ricorsivamente sulla sottostringa senza primo e ultimo carattere.
* Caso base: stringa vuota o con un solo carattere.
'''


def is_palindroma(s: str) -> bool:
    if len(s) <= 1:
        return True
    
    if s[0] != s[-1]:
        return False
    
    return is_palindroma(s[1:-1])

print(is_palindroma("hola"))
print(is_palindroma("ana"))
print(is_palindroma("juana"))
print(is_palindroma(""))