# Esercizio 14
'''
Si scriva una funzione ricorsiva charDuplicator che consenta 
di duplicare ogni carattere in una stringa e restituisca il risultato 
sotto forma di una nuova stringa.

Ad esempio, se la stringa "libro" viene data in input a charDuplicator, 
la funzione ricorsiva deve produrre in output la stringa "lliibbrroo".
'''

def charDuplicator(my_string:str) -> str:

    if my_string == "":
        return ""
    
    else:
        return 2 * my_string[0] + charDuplicator(my_string[1:])

print(f"Il duplicato di ogni carattere di 'libro': {charDuplicator('libro')}")
print(f"Il duplicato di ogni carattere di 'axila': {charDuplicator('axila')}")
print(f"Il duplicato di ogni carattere di 'concentrazione': {charDuplicator('concentrazione')}")