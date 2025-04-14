# Esercizio 9
'''
Si scriva una funzione ricorsiva vowelRemover che elimini 
tutte le vocali da una stringa data e restituisca sotto forma 
di una nuova stringa la stringa originale ma senza le vocali.

Suggerimento: utilizzare l'operatore + per realizzare 
la concatenazione di stringhe al fine di costruire la stringa da restituire.
'''

def vowelRemover(my_string:str) -> str:
    if my_string == "":
        return ""
    else:
        
        if my_string[0] in "aeiou":
            return vowelRemover(my_string[1:])
        
        else:
            return my_string[0] + vowelRemover(my_string[1:])


print(vowelRemover("casa"))