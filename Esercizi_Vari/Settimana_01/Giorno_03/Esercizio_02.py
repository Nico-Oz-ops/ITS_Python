'''
Tema: Uso dei cicli per accumulare valori secondo una condizione

Obiettivo: 
Allenarsi a:
* Usare cicli per esplorare un intervallo di numeri.
* Applicare condizioni (if) per selezionare solo certi elementi (dispari).
* Usare una variabile accumulatore (somma) per tenere traccia di un valore che cresce nel tempo.
'''

# Esercizio 02
# Titolo: "Somma dei numeri dispari"

'''
Traccia:
Scrivi una funzione chiamata somma_dispari() che:

* Chiede all’utente un numero intero positivo maggiore di 0.
* Calcola la somma di tutti i numeri dispari compresi tra 1 e quel numero (incluso).
* Stampa il risultato finale.

Suggerimento:
* Usa try-except per controllare che l’input sia un numero intero valido.
* Per sapere se un numero è dispari, puoi usare: if numero % 2 != 0.
* Crea una variabile chiamata somma = 0 prima del ciclo, e aggiungi ad essa ogni 
numero dispari con somma += num.
'''

def somma_dispari():

    try:
        input_num = int(input("Inserire un numero intero maggiore di 0: "))
    
    except ValueError:
        print("Errore, il numero inserito deve essere intero.")
        return
    if input_num <= 0:
        print("Errore, il numero inserito deve essere maggiore di 0.")
        return
    
    somma_disp = 0
    for num in range(1, input_num + 1):
        if num % 2 != 0:
            somma_disp += num
    print(f"La somma dei numeri dispari tra 1 e {input_num} è: {somma_disp}")    

somma_dispari()




