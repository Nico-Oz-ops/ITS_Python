'''
Tema: Analisi di una lista di numeri

Obiettivo:
Data in input una lista di numeri interi o float, la funzione deve restituire un 
dizionario con informazioni sui valori: minimo, massimo e somma.

Nome dell’esercizio: analyze_numbers

Traccia:
Scrivi una funzione con il seguente header:

* def analyze_numbers(nums: list[float]) -> dict[str, float]:

La funzione deve restituire un dizionario con quattro chiavi:

* "min" → il numero più piccolo della lista
* "max" → il numero più grande della lista
* "sum" → la somma di tutti i numeri
* "average" → la media dei numeri

Vincoli:

Non usare funzioni built-in come min(), max(), sum() o simili.
Non usare librerie esterne.

Se la lista è vuota, solleva un’eccezione ValueError con messaggio "lista vuota".
'''

def analyze_numbers(nums: list[float]) -> dict[str, float]:
    if not nums:
        raise ValueError("Lista vuota")


    num_min = nums[0]
    num_max = nums[0]
    somma = 0.0
    dict_nums = {}

    for num in nums:
        if num < num_min:
            num_min = num
        
        if num > num_max:
            num_max = num
        
        somma += num
    
    media = somma / len(nums)

    dict_nums["min"] = float(num_min)
    dict_nums["max"] = float(num_max)
    dict_nums["somma"] = float(somma)
    dict_nums["average"] = float(media)

    return dict_nums

numeri = [1, 9, 7, 12, 6, 5, 3, 21]
print(analyze_numbers(numeri))






