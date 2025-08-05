'''
Tema: cicli, condizioni, input, media
Obiettivo: calcolare la media aritmetica dei numeri dispari inseriti.
'''

# Esercizio 02
# Titolo: "Media dei numeri dispari"

'''
Traccia:
Scrivi una funzione che chiede all’utente una serie di numeri interi (termina con "fine").
Alla fine stampa la media dei numeri dispari inseriti. 
Se non è stato inserito alcun numero dispari, stampa "Nessun numero dispari inserito".

Suggerimento:
* Tieni due variabili: una per la somma dei dispari, una per contarli.
* Ricorda: un numero è dispari se n % 2 == 1.
'''

def media_dispari() -> None:

    somma_dispari = 0
    cont_dispari = 0

    while True:
        input_num = input("Inserire un numero intero (oppure digitare 'fine' per terminare): ")

        if input_num.strip().lower() == "fine":
            break

        try:
            valore = int(input_num)
            if valore % 2 != 0:
                cont_dispari += 1
                somma_dispari += valore
        except ValueError:
            print("Errore, il valore inserito non è un numero intero.")

    if cont_dispari == 0:
        print("Nessun numero dispari inserito")
    
    else:
        media_dispar = round((somma_dispari / cont_dispari), 2)
        print(f"Media dei numeri dispari inseriti: {media_dispar}")

media_dispari()





