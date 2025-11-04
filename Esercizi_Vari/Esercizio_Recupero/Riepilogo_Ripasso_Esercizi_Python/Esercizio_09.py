'''
Scrivi una funzione che somma tutti i numeri interi di una lista che sono maggiori di un 
dato valore intero definito threshold.

For example:

Test
print(sum_above_threshold([15, 5, 25], 20))
25
'''
def sum_above_threshold(numbers: list[int], valore: int) -> int:
    somma = 0
    for num in numbers:
        if num > valore:
            somma += num
    
    return somma


print(sum_above_threshold([15, 5, 25], 20))

