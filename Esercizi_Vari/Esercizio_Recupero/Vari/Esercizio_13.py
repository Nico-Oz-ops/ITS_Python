'''
Esercizio: Funzione analyze_numbers

Tema: Analisi di una lista di numeri

Obiettivo:
Data una lista di numeri interi o float, la funzione deve restituire un 
dizionario con informazioni sui valori: minimo, massimo, primo e ultimo numericamente.

Nome dell’esercizio: analyze_numbers

Traccia:
Scrivi una funzione con il seguente header:

* def analyze_numbers(nums: list[float]) -> dict[str, float]:


La funzione deve restituire un dizionario con quattro chiavi:

    * "min_value" → il numero più piccolo della lista
    * "max_value" → il numero più grande della lista
    * "first_positive" → il primo numero positivo che appare nella lista
    * "last_negative" → l’ultimo numero negativo che appare nella lista

Vincoli:

* Non usare funzioni built-in come min(), max(), sorted() o simili.
* Non usare librerie esterne.

* Se la lista è vuota, solleva un’eccezione ValueError con messaggio "lista vuota".
* Se non ci sono numeri positivi o negativi, puoi restituire None per quelle chiavi.

Suggerimento:

Itera manualmente sulla lista per confrontare i valori e tenere traccia dei risultati.
Inizializza le variabili con il primo elemento della lista o con None dove appropriato.
'''
def analyze_numbers(nums: list[float]) -> dict[str, float]:
    if not nums:
        raise ValueError("Lista vuota")
    
    num_min = nums[0]
    num_max = nums[0]
    primo_positivo = None
    ultimo_negativo = None
    dict_nums = {}

    for num in nums:
        if num > num_max:
            num_max = num
        
        if num < num_min:
            num_min = num
        
        if num > 0 and primo_positivo is None:
            primo_positivo = num
        
        if num < 0:
            ultimo_negativo = num
        
    dict_nums["min_value"] = float(num_min)
    dict_nums["max_value"] = float(num_max)
    dict_nums["first_positive"] = float(primo_positivo)
    dict_nums["last_negative"] = float(ultimo_negativo)

    return dict_nums