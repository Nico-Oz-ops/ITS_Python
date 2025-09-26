'''
Invoca `letter_count(text)` per restituire un dizionario con 
le occorrenze di ogni lettera alfabetica in minuscolo, 
ignorando simboli, numeri e spazi
'''

def letter_count(text: str) -> dict[str,int]:
    occorrenze = {}

    for lettera in text:
        lettera = lettera.lower()
        if lettera.isalpha(): # verifico se il carattere è una lettera
            if lettera in occorrenze:
                occorrenze[lettera] += 1
            else:
                occorrenze[lettera] = 1
    
    return occorrenze