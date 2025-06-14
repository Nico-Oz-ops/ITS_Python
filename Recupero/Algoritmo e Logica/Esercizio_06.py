# Esercizio 06
'''
Unione di Intervalli Sovrapposti

Data una lista di intervalli chiusi rappresentati come liste di due elementi [start, end],
scrivi una funzione merge_intervals(intervals) che restituisce una nuova lista di
intervalli in cui tutti quelli sovrapposti sono stati fusi. Ogni intervallo soddisfa start <=
end. La lista risultante deve essere ordinata per inizio intervallo e non devono esserci
sovrapposizioni.

Requisiti:

● Input: una lista di liste, ad esempio [[1, 4], [2, 6], [8, 10], [15, 18]].
● Se due intervalli si sovrappongono o si toccano (es. [1,4] e [4,5]), unirli in
[1,5].
● Restituisci una lista di intervalli fusi, ordinata per il valore di inizio.
● Casi limite:
    ○ Se l’input è vuoto, restituisci una lista vuota.
    ○ Se è presente un solo intervallo, restituiscilo così com’è.

Esempi:
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
merge_intervals(intervals) # restituisce [[1, 6], [8, 10], [15,
18]]
intervals = [[1, 4], [4, 5]]
merge_intervals(intervals) # restituisce [[1, 5]]
'''

def merge_intervals(intervals: list[list[int]]):
    
    intervals.sort()

    if not intervals:
        return []
    
    if len(intervals) == 1:
        return intervals
    
    unione = [intervals[0]]

    for inter_attuale in intervals[1:]:
        ultimo_intervallo = unione[-1]

        if inter_attuale[0] > inter_attuale[1]:
            raise ValueError(f"Errore, intervallo non valido '[{inter_attuale[0]}, {inter_attuale[1]}]'")
        
        if inter_attuale[0] <= ultimo_intervallo[1]:
            ultimo_intervallo[1] = max(ultimo_intervallo[1], inter_attuale[1])
        
        else: 
            unione.append(inter_attuale)
    
    return unione


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_intervals(intervals))
