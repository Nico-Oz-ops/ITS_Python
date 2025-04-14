# Esercizio 8
'''
Si scriva una funzione ricorsiva vowelsCounter che 
conti il numero di vocali in una stringa.

Suggerimento: ogni volta che si effettua una chiamata ricorsiva, 
si utilizzi lo slicing per ottenere una nuova stringa formata dai caratteri 
compresi tra il secondo e l'ultimo della stringa originale.
L'ultima chiamata ricorsiva avverrà quando la stringa non contiene caratteri.
'''

def vowelsCounter(stringa:str) -> int:

    if stringa == "":
        return 0
    
    else:
        if stringa[0] in "aeiou":
            return 1 + vowelsCounter(stringa[1:])
        
        else:
            return vowelsCounter(stringa[1:])

print(vowelsCounter("paralelepipedo"))

# a i u t o  
# 0 1 2 3 4 

# a i u t o
# i u t o 
# u t o 
# t o 
# o