'''
Tema: Liste e Posizioni
Obiettivo: Saper usare in modo efficace:

* gli indici
* le sottoliste
* il controllo sulle posizioni
* e le liste come struttura dinamica
'''

# Esercizio 01
# Titolo: "Somma degli elementi in posizione multipla di 3"

'''
Traccia:
Scrivi una funzione che riceve una lista di numeri e restituisce la somma dei numeri che 
si trovano in posizione multipla di 3 (quindi indice 0, 3, 6, 9...).
'''
# Opzione A - lavora sulla posizione
def somma_posizione_multipla_di_3(num: list[int]) -> int:
    return sum(num[i] for i in range(0, len(num), 3))

print(somma_posizione_multipla_di_3([4, 2, 7, 9, 1, 6, 8, 3, 5, 10]))

# Opzione B - lavora sulla posizione
def somma_posizione_multipla_di_3_b(nums: list[int]) -> int:
    somma_mult_3 = 0

    for i in range(0, len(nums), 3):
        somma_mult_3 += nums[i]
    return somma_mult_3
print(somma_posizione_multipla_di_3_b([5, 3, 8, 11, 6, 52, 8, 3, 5, 10]))

# Opzione C - lavora sul valore
def somma_posizione_multipla_di_3_c(nums: list[int]) -> int:
    somma_mult_3 = 0

    for i in range(0, len(nums)):
        if nums[i] % 3 == 0:
            somma_mult_3 += nums[i]
    return somma_mult_3
print(somma_posizione_multipla_di_3_c([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

