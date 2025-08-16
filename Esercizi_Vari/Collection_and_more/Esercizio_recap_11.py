'''
Tema: Liste e condizioni
Obiettivo: Ripassare l’uso dei cicli e delle condizioni sugli elementi.

Nome dell’esercizio: numeri_pari_grandi

Traccia:
Scrivi una funzione che, data una lista di numeri interi e una soglia, 
ritorni una nuova lista contenente solo i numeri pari maggiori della soglia.

Esempio:
numeri = [2, 15, 8, 23, 10, 4], soglia = 7  
→ risultato = [8, 10]

Suggerimento: Usa un ciclo for con un if per filtrare.
'''

def numeri_pari_grandi(numeri: list[int], soglia: int) -> list[int]:
    return [numero for numero in numeri if numero % 2 == 0 and numero > soglia]

numeri = [2, 15, 8, 23, 10, 4]
soglia = 7  
print(numeri_pari_grandi(numeri, soglia))