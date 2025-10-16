'''
Titolo dell’esercizio: Analisi dei numeri pari e dispari
 
Obiettivo
Scrivi una funzione che prende in input una lista di numeri interi e restituisce un 
dizionario con le seguenti informazioni:
 
* Il numero pari più piccolo
* Il numero dispari più grande
* Il conteggio totale dei numeri pari
* Il conteggio totale dei numeri dispari
 
Header della funzione
* def analyze_even_odd(nums: list[int]) -> dict[str, int | None]:
 
Requisiti
 
* Non puoi usare funzioni già pronte come min, max, filter, sorted o simili
* Se la lista è vuota, devi sollevare un ValueError con il messaggio "lista vuota"
* Se non ci sono numeri pari o dispari, per quei valori nel dizionario puoi restituire None
'''

def analyze_even_odd(nums: list[int]) -> dict[str, int | None]:
    if not nums:
        raise ValueError("Lista vuota")

    num_par_piccolo = None
    num_disp_grande = None
    count_par = 0
    count_dispar = 0
    my_dict = {}

    for num in nums:
        if num % 2 == 0:
            count_par += 1
            if num_par_piccolo is None or num < num_par_piccolo:
                num_par_piccolo = num
        
        else:
            count_dispar += 1
            if num_disp_grande is None or num > num_disp_grande:
                num_disp_grande = num

    my_dict["numero pari più piccolo"] = num_par_piccolo
    my_dict["numero dispari più grande"] = num_disp_grande
    my_dict["totale numeri pari"] = count_par
    my_dict["totale numeri dispari"] = count_dispar

    return my_dict

numeri = [1, 8, 6, 7, 2, 5, 8, 89]
print(analyze_even_odd(numeri))
