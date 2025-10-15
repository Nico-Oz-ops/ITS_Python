'''
Scrivi una funzione con il seguente header:

calculate_stats(nums: list[float]) -> dict[str, float]

che, data una lista di numeri, ritorni un dizionario con tre chiavi:
    * "min" -> il valore minimo della lista
    * "max" -> il valore massimo della lista
    * "avg" -> la media aritmetica (somma diviso numero di elementi)

Se la lista è vuota, solleva un'eccezione ValueError con messaggio "lista vuota

Attenzione i valori min, max e avg non possono essere calcolati usando funzioni built-in di python  
o altre librerie
'''

def calculate_stats(nums: list[float]) -> dict[str, float]:
    dict_nums = {}
    massimo = nums[0]
    minimo = nums[0]
    somma = 0

    for num in nums:
        somma += num

        if num > massimo:
            massimo = num
        
        if num < minimo:
            minimo = num
    media = somma / len(nums)
    
    dict_nums["min"] = minimo
    dict_nums["max"] = massimo
    dict_nums["avg"] = media

    return dict_nums

numeri = [10, 3, 7.5, -2, 15]
print(calculate_stats(numeri))


print(numeri.remove(2))
