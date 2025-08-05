'''
Obiettivo: 
Allenarti a:
* usare i cicli for e le condizioni per filtrare numeri
* calcolare la somma dei numeri pari in un intervallo scelto dall’utente
'''

# Esercizio 03
# Titolo: "Somma dei pari"

'''
Traccia:
Scrivi una funzione chiamata somma_pari() che:
* Chiede all’utente di inserire un numero intero positivo N
* Calcola e stampa la somma di tutti i numeri pari da 1 a N (incluso)
* Se l’input non è valido (non intero o non positivo), stampa un messaggio di errore e termina

Suggerimenti:
* Usa range(1, N+1) per scorrere i numeri da 1 a N
* Controlla se un numero è pari con numero % 2 == 0
* Usa una variabile somma per accumulare il totale
'''

def somma_pari() -> int:
    try:
        input_num = int(input("Inserire un numero intero positivo: "))
    
    except ValueError:
        print("Errore, il numero inserito non è un intero")
        return
    
    if input_num <= 0:
        print("Errore, il numero inserito non è positivo")
        return

    somma = 0
    for num in range(1, input_num + 1):
        if num % 2 != 0:
            continue
        somma += num
    return f"Somma dei numeri pari da 1 a {input_num}: {somma}"

print(somma_pari())