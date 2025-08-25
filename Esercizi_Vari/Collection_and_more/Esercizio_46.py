'''
Filtra numeri pari e dispari

Tema: Liste e dizionari
Obiettivo: Separare numeri in base alla parità

Nome: pari_dispari

Traccia:
Scrivi una funzione pari_dispari(numeri: list[int]) -> dict[str, list[int]] 
che ritorni un dizionario con chiavi "pari" e "dispari" e valori le rispettive liste di numeri.

Input:
numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''
def pari_dispari(numeri: list[int]) -> dict[str, list[int]]:
    risultato = {"pari": [], "dispari": []}

    for numero in numeri:
        if numero % 2 == 0:
            risultato["pari"].append(numero)
        
        else:
            risultato["dispari"].append(numero)
    
    return risultato

numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(pari_dispari(numeri))