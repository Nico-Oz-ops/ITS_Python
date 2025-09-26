'''
Esercizio - 01
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
'''
# Alternativa 1
def ordina_per_lunghezza_chiave(dati: dict[str, int]) -> list[tuple[str,int]]:
    lista_tuple = list(dati.items())
    lunghezza = len(lista_tuple)

    for i in range(lunghezza):
        for j in range (0, lunghezza - i - 1):
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

# Alternativa 2
def ordina_per_lunghezza_chiave(dati: dict[str, int]) -> list[tuple[str,int]]:
    return sorted(dati.items(), key=lambda x: len(x[0]))

dati = {
    "Anna": 24,
    "Luca": 30,
    "Martina": 21,
    "Al": 40
}
print(ordina_per_lunghezza_chiave(dati))


# Alternativa 3
def ordina_per_lunghezza_chiave(dati: dict[str, int]) -> list[tuple[str,int]]:
    return [elemento for elemento in sorted(dati.items(), key=lambda elemento: len(elemento[0]))]

print(ordina_per_lunghezza_chiave(dati))