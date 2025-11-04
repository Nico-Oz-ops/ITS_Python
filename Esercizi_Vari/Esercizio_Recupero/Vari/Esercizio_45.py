'''
Tema: Liste e manipolazioni
Obiettivo: Ruotare gli elementi di una lista di un numero specifico di posizioni

Nome dell’esercizio: rotate_list

Traccia: Scrivi una funzione chiamata rotate_list che prenda una lista di 
numeri e un intero k, e restituisca una nuova lista in cui gli elementi sono 
ruotati di k posizioni verso destra. Se k è negativo, la rotazione avverrà verso sinistra.

Suggerimento: Puoi usare slicing per ottenere la rotazione in maniera elegante.
'''
# Opzione 1
def rotate_list(numeri: list[int], k: int) -> list[int]:
    if not numeri:
        return []
    
    n = len(numeri)
    k = k % n # normnalizzo k per evitare rotazioni inutili

    return numeri[-k:] + numeri[:-k] 
    # -k: indica partire dalla fine della lista contando k elementi indietro
    # :-k indica tutti gli elementi tranne gli ultimi k
    # + concatena le due liste

# Opzione 2
def rotate_list(nums: list[int], k: int) -> list[int]:
    if not nums:
        return []
    
    n = len(nums)
    k = k % n

    if k < 0: # si rota verso sinistra
        k = n + k # così equivale a rotare a destra
    
    rotazione = [0] * n # list con la stessa lunghezza di nums, inizializzata con zeri. Conterrà gli elementi ruotati
    for i in range(n): #i va da 0 a n-1 e rappresenta l’indice originale in nums
        # (i + k) % n calcola il nuovo indice dove posizionare l’elemento nella lista ruotata
        # % n serve a “riciclare” gli indici quando superano la lunghezza della lista (wrap-around)
        # rotated[(i + k) % n] = nums[i] sposta l’elemento nums[i] nella sua nuova posizione
        rotazione[(i + k) % n] = nums[i]
    
    return rotazione


# % n serve per assicurarsi che gli indici restino all’interno della lista dopo la rotazione


# Test
print(rotate_list([1, 2, 3, 4, 5], 2))   
print(rotate_list([1, 2, 3, 4, 5], -2))  
print(rotate_list([], 3)) 