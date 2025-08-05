'''
Tema: Input multiplo con while, filtri, contatori e uso della divisione

Obiettivo:
Allenarti a:

* Gestire input multipli con ciclo while
* Filtrare i numeri: considerare solo i positivi
* Calcolare una media aritmetica
* Usare try-except, contatore e sommatore

'''

# Esercizio 04
# Titolo: "Media dei numeri positivi"

'''
Traccia:
Scrivi una funzione media_numeri_positivi() che:

* Chiede numeri interi all’utente in un ciclo infinito.
* Termina quando l’utente scrive "stop".
* Tiene conto solo dei numeri maggiori di zero.

Alla fine stampa:
* Il numero di valori positivi inseriti
* La media aritmetica dei numeri positivi
* Se non è stato inserito nessun numero positivo, stampa un messaggio specifico.
'''

def media_numeri_positivi():
    cont_positivi = 0
    somma_positivi = 0

    while True:
        input_num = input("Inserire un numero intero positivo: ")

        if input_num.lower() == "stop":
            break

        try:
            valore = int(input_num)
            if valore > 0:
                cont_positivi += 1
                somma_positivi += valore

        except ValueError:
            print("Errore, il numero inserito non è un numero intero")
    
    media_positivi = round(somma_positivi / cont_positivi, 2)

    if cont_positivi > 0:
        print(f"\nNumero di valori positivi inseriti: {cont_positivi}")
        print(f"Media artimetica dei valori inseriti: {media_positivi}")

    else:
        print("Non è stato inserito nessun valore positivo")

media_numeri_positivi()
    









