# Esercizio 03
'''
Scrivi una funzione che codifica le lettere

Descrizione:
Scrivi una funzione chiamata codifica_lettere(s, chiave) che:

prende una stringa s e una chiave numerica (ad esempio 2),

per ogni lettera minuscola, la sposta avanti di chiave posizioni nell'alfabeto,

lascia invariati gli altri caratteri (spazi, punteggiatura, numeri…),

restituisce la nuova stringa cifrata.

Suggerimenti:

Usa from string import ascii_lowercase

Ricorda di usare ascii_lowercase.index(char) per trovare l'indice

Usa % 26 per non uscire fuori dall'alfabeto

Non dimenticare lista.append(...) e alla fine ''.join(lista)
'''

from string import ascii_lowercase, ascii_uppercase

def codifica_lettere(s, chiave):
    
    str_cifrata = []

    for car in s:
        if car in ascii_lowercase:
            indice = (ascii_lowercase.index(car) + chiave) % 26
            str_cifrata.append(ascii_lowercase[indice])
        
        elif car in ascii_uppercase:
            indice = (ascii_uppercase.index(car) + chiave) % 26
            str_cifrata.append(ascii_uppercase[indice])
        
        else:
            str_cifrata.append(car)
    
    return ''.join(str_cifrata) # in questo modo restitusice una stringa -> Ekcq Oqpfq! 
                                # invece "return str_cifrata" avrebbe restituito una lista di caratteri -> ['E', 'k', 'c', 'q', ' ', 'O', 'q', 'p', 'f', 'q', '!']


print(codifica_lettere("Ciao Mondo!", 2))

