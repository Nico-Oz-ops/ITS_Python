# Esercizio 12
'''
Si scriva una funzione ricorsiva vowelsCounter che conti il numero di vocali in una stringa.

Suggerimento: ogni volta che si effettua una chiamata ricorsiva, si utilizzi lo slicing per 
ottenere una nuova stringa formata dai caratteri compresi tra il secondo e l'ultimo della stringa originale.
L'ultima chiamata ricorsiva avverrà quando la stringa non contiene caratteri.
'''

def vowelsCounter(my_string:str) -> int:

    if my_string == "":
        return 0
    
    else:
        if my_string[0] in "aeiou":
            return int(1 + vowelsCounter(my_string[1:]))
        
        else:
            return int(vowelsCounter(my_string[1:]))

print(f"La parola \"computer\" ha: {vowelsCounter('computer')} cifre.")
print(f"La parola \"orchidea\" ha: {vowelsCounter('orchidea')} cifre.")
print(f"La parola \"narcismo\" ha: {vowelsCounter('narciso')} cifre.")  