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

    for i in range(n):
        for j in range(0, n - i - 1):
            if len(lista_tuple[j][0]) > len(lista_tuple[j + 1][0]):
                lista_tuple[j], lista_tuple[j + 1] = lista_tuple[j + 1], lista_tuple[j]
    
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