'''
Tema: Cicli, condizioni, funzioni e collections
Obiettivo:
Consolidare le basi con più esercizi brevi e progressivi.
'''

# Esercizio 01
# Titolo: "Somma dei numeri positivi"

'''
Traccia:
Scrivi una funzione che continua a chiedere all’utente dei numeri interi finché non digita "stop".
A quel punto stampa la somma solo dei numeri positivi inseriti.

Suggerimento: usa un ciclo while con input() e la funzione int() 
solo dopo aver verificato che l’input non sia "stop".
'''

def somma_positivi() -> None:

    somma = 0
    while True:

        input_num = input("Inserire un numero intero positivo alla volta (oppure digitare 'stop' per terminare): ")

        if input_num == "stop":
            break

        try:
            valore = int(input_num)
            if valore > 0:
                somma += valore
                
        except ValueError:
            print("Errore, il valore inserito non è un numero intero positivo.")
    
    print(f"Somma dei numeri interi positivi inseriti: {somma}")

somma_positivi()
        
    
