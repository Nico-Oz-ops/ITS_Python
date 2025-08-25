'''
Tema: Dizionari - Raggruppamento
Obiettivo: Creare categorie.

Nome dell’esercizio: Raggruppa numeri pari e dispari

Traccia:
Scrivi una funzione raggruppa_pari_dispari(numeri: list[int]) -> dict[str, list[int]] che, 
data una lista di numeri, ritorni un dizionario con due chiavi: "pari" e "dispari".

Nella lista "pari" vanno tutti i numeri pari, in "dispari" tutti i numeri dispari.

numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Suggerimento:
Puoi inizializzare il dizionario con le due chiavi già pronte e aggiungere i numeri scorrendo la lista.
'''
# Alternativa 1
def raggruppa_pari_dispari(numeri: list [int]) -> dict[str, list[int]]:
    risultato = {"pari": [], "dispari": []}

    for numero in numeri:
        if numero % 2 == 0:
            risultato["pari"].append(numero)
        else:
            risultato["dispari"].append(numero)
    
    return risultato
    
numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(raggruppa_pari_dispari(numeri))

