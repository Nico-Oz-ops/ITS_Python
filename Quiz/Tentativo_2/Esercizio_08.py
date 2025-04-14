# Esercizio 8
'''Scrivi una funzione che conta e ritorna quante volte un elemento appare isolato in una lista di numeri interi. 
Un elemento è considerato isolato se non è affiancato sia a destra che a sinistra da elementi uguali.
'''

def cont_isolato(num_interi:list[int]) -> int:
    contatore = 0

    for elemento in range(len(num_interi)):
        if (elemento == 0 or num_interi[elemento] != num_interi[elemento - 1]) and (elemento == len(num_interi) - 1 or num_interi[elemento] != num_interi[elemento + 1]):
            contatore += 1
    
    return contatore



print(cont_isolato([1, 2, 2, 3, 3, 3, 4]))
print(cont_isolato([1, 2, 3, 4, 5]))

# Caso 2 (opzionale) - se volessi conteggiare i numeri che si ripetono 

def conteggio_ripetuti(num_interi:list[int]) -> dict[int, int]:

    conteggio = {} # creo un dizionario per memorizzare il conteggio di ogni elemento

    for elemento in num_interi:
        if elemento in conteggio:
            conteggio[elemento] += 1 # incremento il conteggio se l'elemento è già nel dizionario conteggio {}
        
        else:
            conteggio[elemento] = 1 # altrimenti (se l'elemento non si trova), aggiungo l'elemento con conteggio 1

# filtro gli elementi che si ripetono, cioè quelli con conteggio maggiore di 1
    ripetizione = {key: value for key, value in conteggio.items() if value > 1}

    return ripetizione

print(conteggio_ripetuti([1, 1, 1, 2, 6, 3, 3, 4, 5, 4, 8, 5, 6, 7, 6, 6, 6, 6]))