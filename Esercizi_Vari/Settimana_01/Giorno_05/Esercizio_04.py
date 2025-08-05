'''
Tema: Cicli, numeri e condizioni
Obiettivo: Stampare tutti i numeri tra 1 e 100 divisibili sia per 3 che per 5.
'''

# Esercizio 04
# Titolo: "Numeri divisibili per 3 e 5"

'''
Traccia:
Scrivi una funzione divisibili_tre_cinque() -> None che:

* Scorra i numeri da 1 a 100 (inclusi).
* Per ciascun numero, verifichi se è divisibile sia per 3 che per 5.
* Se lo è, lo stampi a video.
'''

def divisibili_tre_cinque() -> None:
    for num in range(1, 100):
        if num % 3 == 0 and num % 5 == 0:
            print(num)

divisibili_tre_cinque()

# oppure

def divisibili_tre_cinque() -> None:
    for num in range(1, 100):
        if num % 3 == 0 and num % 5 == 0:
            print(num, end=" ")

divisibili_tre_cinque()






