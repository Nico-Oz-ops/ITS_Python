'''
Obiettivo: 
Allenarti con:
* Cicli
* Condizioni multiple (if, elif, else)
* Riconoscere i multipli di un numero
'''

# Esercizio 05
# Titolo: "Conta FizzBuzz"

'''
Traccia:
Scrivi una funzione fizzbuzz() che:

* Chiede all’utente di inserire un numero intero positivo N
* Scorre tutti i numeri da 1 a N inclusi

Per ogni numero:

* Se è multiplo sia di 3 che di 5, stampa "FizzBuzz"
* Se è solo multiplo di 3, stampa "Fizz"
* Se è solo multiplo di 5, stampa "Buzz"
* Altrimenti stampa il numero stesso

Suggerimenti:
* Un numero è multiplo di 3 se num % 3 == 0
* Un numero è multiplo di 5 se num % 5 == 0
* La condizione multiplo di 3 e 5 va prima delle altre, altrimenti viene “saltata”
'''

def fizzbuzz():

    try:
        input_num = int(input("Inserire un numero intero positivo: "))
    
    except ValueError:
        print("Errore, il numero inserito deve essere intero")
        return
    if input_num <= 0:
        print("Errore, il numero inserito deve essere positivo")
        return
    
    for num in range(1, input_num + 1):
        if num % 3 == 0 and num % 5 == 0:
            print("Fizzbuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

fizzbuzz()