'''
Tema: Liste e condizioni
Obiettivo: Ripassare cicli e confronto tra elementi.

Nome dell’esercizio: elementi_unici

Traccia:
Scrivi una funzione che, data una lista di numeri, ritorni una nuova lista 
contenente solo gli elementi che compaiono una sola volta.

Esempio:
numeri = [4, 5, 4, 6, 7, 5, 8]  
→ risultato = [6, 7, 8]

Suggerimento: Puoi usare il metodo count() oppure un dizionario/set di supporto.
'''
# Alternativa 1
def elementi_unici(numeri: list[int]) -> list[int]:
    return [numero for numero in numeri if numeri.count(numero) == 1]

numeri = [4, 5, 4, 6, 7, 5, 8]  
print(elementi_unici(numeri))

# Alternartiva 2
def elementi_unici(numeri: list[int]) -> list[int]:
    risultato = {}

    for numero in numeri:
        if numero not in risultato:
            risultato[numero] = 1
        else:
            risultato[numero] += 1
    
    return [numero for numero in risultato if risultato[numero] == 1]
numeri = [4, 5, 4, 6, 7, 5, 8]  
print(elementi_unici(numeri))