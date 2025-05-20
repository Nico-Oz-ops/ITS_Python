# Esercizio 3
'''
Scrivi una funzione che elimini dalla lista dati certi 
elementi specificati in un dizionario.
Il dizionario contiene elementi da rimuovere come chiavi e 
il numero di volte che devono essere rimossi come valori.
'''

def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:

    for elemento, volte in da_rimuovere.items():
        for item in range(volte):
            if elemento in lista:
                lista.remove(elemento)
    
    return lista

print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 2}))
print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 1}))
print(rimuovi_elementi([1, 1, 1, 1], {1: 2}))
print(rimuovi_elementi([4, 5, 6], {1: 3}))
print(rimuovi_elementi([], {2: 1}))

