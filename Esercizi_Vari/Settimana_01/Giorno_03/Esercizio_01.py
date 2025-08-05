'''
Tema: Filtrare valori con condizioni e cicli

Obiettivo: Scrivere un programma che chiede all’utente un numero intero positivo e 
stampa tutti i numeri primi minori o uguali a quel numero.
'''

# Esercizio 01
# Titolo: "Numeri Primi fino a N"

'''
Crea una funzione chiamata stampa_numeri_primi() che:

* Chiede all’utente un numero intero positivo.
* Controlla che l'input sia valido (deve essere un intero > 1).
* Stampa tutti i numeri primi da 2 fino a quel numero, uno per riga.

Suggerimento: un numero è primo se è maggiore di 1 e ha solo due divisori: 1 e sé stesso. 
Puoi usare un ciclo for annidato per controllarlo.
'''

def stampa_numeri_primi():

    try:
        input_num = int(input("Inserire un numero intero positivo: "))
    
    except ValueError:
        print("Errore, il numero inserito non è un intero")
        return
    
    if input_num < 0:
        print("Errore, il numero inserito non è un numero intero positivo")
        return

    for num in range(2, input_num + 1):
        
        num_primo = True
        for i in range(2, num):
            if num % i == 0:
                num_primo = False
                break

        if num_primo:
            print(num)

stampa_numeri_primi()




    



