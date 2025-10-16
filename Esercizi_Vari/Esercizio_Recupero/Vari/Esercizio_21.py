'''
calculate_normalized_scores

Scrivi una funzione chiamata

* calculate_normalized_scores(scores: list[float]) -> list[float]

che restituisca una nuova lista con tutti i punteggi normalizzati tra 0 e 1, secondo la formula:
valore normalizzato = x - min / max - min

Regole:

Se la lista è vuota, solleva ValueError("lista vuota").

Se tutti i valori nella lista sono uguali (quindi max == min), solleva un 
ZeroDivisionError("impossibile normalizzare: valori uguali")

Esempio:

calculate_normalized_scores([10, 20, 30])  # ➜ [0.0, 0.5, 1.0]
'''

def calculate_normalized_scores(scores: list[float]) -> list[float]:
    if not scores:
        raise ValueError("Lista vuota")
    
    minimo = scores[0]
    massimo = scores[0]

    for num in scores:
        if num < minimo:
            minimo = num
        if num > massimo:
            massimo = num
        
    if massimo == minimo:
        raise ZeroDivisionError("Impossibile normalizzare: valori uguali")
    

    punteggi_normalizzati = []

    for num in scores:
        valore_normalizzato = (num - minimo) / (massimo - minimo)
        punteggi_normalizzati.append(float(valore_normalizzato))
    
    return punteggi_normalizzati

scores = [10, 20, 30]
print(calculate_normalized_scores(scores))
