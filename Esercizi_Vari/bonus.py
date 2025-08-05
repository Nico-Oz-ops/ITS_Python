'''scrivi una funzione che somma i numeri che hanno indice pari. 
Ti viene fornita questa lista:  [5, 8, 12, 7, 3, 10]'''

# Opzione A
def somma_indice_pari(lista: list[int]) -> int:
    somma = 0

    for i in range(0, len(lista), 2):
        somma += lista[i]
    
    return somma

print(somma_indice_pari([5, 8, 12, 7, 3, 10]))


# Opzione B
def somma_indice_pari_2(lista: list[int]) -> int:
    return sum(lista[i] for i in range(0, len(lista), 2))

print(somma_indice_pari_2([5, 8, 12, 7, 3, 10]))


# Opzione C - Somma indici dispari
def somma_indici_dispari(list_num: list[int]) -> int:
    return sum(list_num[i] for i in range(1, len(list_num), 2))

print(somma_indici_dispari([1, 6, 8, 11, 4, 8, 3, 0]))




