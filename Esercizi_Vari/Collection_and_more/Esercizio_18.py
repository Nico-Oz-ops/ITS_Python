'''
Tema: Dizionari e ordinamento
Obiettivo: Ripassare come ordinare i dati in base ai valori.

Nome dell’esercizio: ordina_per_valore

Traccia:
Scrivi una funzione che prenda in input un dizionario con chiavi stringa e valori numerici, 
e restituisca una lista di tuple ordinate in base ai valori, dal più alto al più basso.
 
Esempio:
dati = {
    "Anna": 24,
    "Luca": 30,
    "Marta": 21
}
Output desiderato:
[('Luca', 30), ('Anna', 24), ('Marta', 21)]

Suggerimento: Puoi usare la funzione built-in sorted() con key per ordinare in base ai valori.
'''
# Alternativa 1 - bubble sort
def ordina_per_valore(dati: dict[str, int]) -> list[tuple[str, int]]:
    lista_tuple = list(dati.items())
    n = len(lista_tuple)

    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_tuple[j][1] < lista_tuple[j + 1][1]:
                lista_tuple[j], lista_tuple[j + 1] = lista_tuple[j + 1], lista_tuple[j]
    
    return lista_tuple

dati = {
    "Anna": 24,
    "Luca": 30,
    "Marta": 21
}

print(ordina_per_valore(dati))

# Alternativa 2 - sorted() and key
def ordina_per_valore(dati: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(dati.items(), key=lambda elemento: elemento[1], reverse=True)

dati = {
    "Anna": 24,
    "Luca": 30,
    "Marta": 21
}

print(ordina_per_valore(dati))
        



