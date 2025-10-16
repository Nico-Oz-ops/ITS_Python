'''
Traccia esercizio: scale_to_range

Tema: Normalizzazione e trasformazioni di liste di numeri

Obiettivo:
Scrivi una funzione che prende in input una lista di numeri e un intervallo [new_min, new_max] 
e restituisce una nuova lista in cui tutti i valori sono scalati nel nuovo intervallo, secondo la formula:

valore_scalato = new_min + (x - min) / (max - min) * (new_max - new_min)

Nome dell’esercizio: scale_to_range

Header della funzione:
def scale_to_range(values: list[float], new_min: float, new_max: float) -> list[float]:

Regole:

* Non usare funzioni built-in come min(), max(), map() o simili.
* Se la lista è vuota, solleva ValueError("lista vuota").
* Se tutti i valori della lista sono uguali (quindi max == min), 
solleva ZeroDivisionError("impossibile scalare: valori uguali").

Esempio:

scale_to_range([10, 20, 30], 0, 100)  # ➜ [0.0, 50.0, 100.0]
scale_to_range([5, 5, 5], 0, 10)      # ➜ solleva ZeroDivisionError
'''
def scale_to_range(values: list[float], new_min: float, new_max: float) -> list[float]:
    if not values:
        raise ValueError("Lista vuota")
    
    val_max = values[0]
    val_min = values[0]

    for num in values:
        if num > val_max:
            val_max = num
        
        if num < val_min:
            val_min = num
    
    if val_max == val_min:
        raise ZeroDivisionError("Impossibile scalare: valori uguali")
    

    valori_scalati = []
    for num in values:
        val_scalato = new_min + (num - val_min) / (val_max - val_min) * (new_max - new_min)
        valori_scalati.append(float(val_scalato))
    
    return valori_scalati

scores = [10, 20, 30]
new_massimo = 100
new_minimo = 0

print(scale_to_range(scores, new_minimo, new_massimo))
