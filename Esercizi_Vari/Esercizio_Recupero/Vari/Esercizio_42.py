'''
Statistiche

Scrivi una funzione con il seguente header:

* calculate_stats(nums: list[float]) -> dict[str, float]:

che, data una lista di numeri, ritorni un dizionario con tre chiavi:

* "min" -> il valore minimo della lista
* "max" -> il valore massimo della lista
* "avg" -> la media aritmetica (somma diviso numero di elementi)

Se la lista è vuota, solleva un'eccezione ValueError con messaggio "lista vuota"

Attenzione, i valori min. max e avg non possono essere calcolati usando funzioni built-in di python o altre librerie.
'''

def calculate_stats(nums: list[float]) -> dict[str, float]:
    if not nums:
        raise ValueError("Lista vuota")

    dict_stats = {}

    val_min = nums[0]
    val_max = nums[0]
    somma = 0.0

    for num in nums:
        if num < val_min:
            val_min = num
        
        if num > val_max:
            val_max = num
        
        somma += num
    
    media = somma / len(nums)
    
    dict_stats["min"] = float(val_min)
    dict_stats["max"] = float(val_max)
    dict_stats["avg"] = float(media)

    return dict_stats


print(calculate_stats([3, 7, 2, 9, 5]))
