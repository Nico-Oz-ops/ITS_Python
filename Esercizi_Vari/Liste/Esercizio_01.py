'''
Esercizio 1

Tema: Liste e valori unici
Obiettivo: Lavorare con insiemi e filtri

Nome dell’esercizio: Elementi unici in una lista

Traccia:
Scrivi una funzione elementi_unici(lista) che, data una lista di numeri, 
ritorni una nuova lista contenente solo gli elementi che compaiono una sola volta.

Esempio: 
elementi_unici([1, 2, 2, 3, 4, 4, 5])  
'''
# Alternativa 1
def elementi_unici(elementi: list[int]):
    return [elemento for elemento in elementi if elementi.count(elemento) == 1]

elementi = [1, 2, 2, 3, 4, 4, 5]
print(elementi_unici(elementi))

# Alternativa 2
def elementi_unici(elementi: list[int]):
    conteggio = {}
    
    for elemento in elementi:
        if elemento not in conteggio:
            conteggio[elemento] = 1        
        else:
            conteggio[elemento] += 1
    
    risultato = []
    for elemento in conteggio:
        if conteggio[elemento] == 1:
            risultato.append(elemento)
    
    return risultato

elementi = [1, 2, 2, 3, 4, 4, 5]
print(elementi_unici(elementi))

# Alternativa 3
def elementi_unici(elementi: list[int]):
    return list(filter(lambda elemento: elementi.count(elemento) == 1, elementi))


