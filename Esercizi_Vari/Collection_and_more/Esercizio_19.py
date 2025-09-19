'''
Tema: Dizionari e stringhe
Obiettivo: Ripassare l’ordinamento in base a una caratteristica delle chiavi.

Nome dell’esercizio: ordina_per_lunghezza_chiave

Traccia:
Scrivi una funzione che prende un dizionario con chiavi stringa e valori 
qualsiasi e restituisce una lista di tuple ordinate in base alla lunghezza delle chiavi in ordine crescente.
 
Esempio:
dati = {
    "Anna": 24,
    "Luca": 30,
    "Martina": 21,
    "Al": 40
}
Output desiderato:
[('Al', 40), ('Anna', 24), ('Luca', 30), ('Martina', 21)]

Suggerimento: Usa sorted() con key=len per confrontare la lunghezza delle chiavi.
'''
# Alternativa 1 - bubble sort
def ordina_per_lunghezza_chiave(dati: dict[str, int]) -> list[tuple[str, int]]:
    lista_tuple = list(dati.items())
    n = len(lista_tuple)

    for i in range(n): # ciclo esterno (i) - conta le "passate" sull'intera lista (quante volte ripeto i confronti)
                       # ad ogni passata l'elemento più grande finisce in fondo alla lista, quindi non serve più ricontrollarlo nelle passate successive 
        for j in range(0, n - i - 1): # ciclo interno (j) - confronto elemento per elemento nella parte non ancora ordinata della lista.
                                      # con "n - i - 1" evito di ricontrollare gli ultimi elementi già ordinati
            if len(lista_tuple[j][0]) > len(lista_tuple[j + 1][0]): # confronto la lunghezza della stringa contenuta nel primo elemento di ciascuna tupla
                                                                    # se la stringa in posizione j è più lunga di quella in posizione j + 1, bisogna scambiarle
                lista_tuple[j], lista_tuple[j + 1] = lista_tuple[j + 1], lista_tuple[j] # scambia le due tuple: quella con la stringa più corta va prima
    
    return lista_tuple

dati = {
    "Anna": 24,
    "Luca": 30,
    "Martina": 21,
    "Al": 40
}
print(ordina_per_lunghezza_chiave(dati))

# Alternativa 2 - sorted() and key
def ordina_per_lunghezza_chiave(dati: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(dati.items(), key=lambda elemento: len(elemento[0]), reverse=False)

dati = {
    "Anna": 24,
    "Luca": 30,
    "Martina": 21,
    "Al": 40
}
print(ordina_per_lunghezza_chiave(dati))