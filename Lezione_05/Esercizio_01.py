# Esercizio 1 - Simulazione: La tartaruga e la lepre
import random

def percorso(posizione_tarta, posizione_lepre):
    percorso = ["_"] * 70 # lista vuota con 70 posizioni

    if posizione_tarta == posizione_lepre:
        percorso[min(posizione_tarta, 69)] = "OUCH!"  # aggiungo la collisione solo se le posizioni sono uguali, gestisco la collisione
        print("OUCH!")
# se la tartaruga o la lepre tentano di occupare una posizione fuori dalla lista (oltre la posizione 70), il codice userà comunque l'ultimo indice valido (69).
    else:
        percorso[min(posizione_tarta - 1, 69)] = "T" # metto la tartaruga nella sua posizione
        percorso[min(posizione_lepre - 1, 69)] = "H" # metto la lepre nella sua posizione
    
    print(" ".join(percorso)) # la lista delle posizioni le unisco in una singola stringa, separandole con uno spazio


def mossa_tartaruga(posizione_tart:int):
    mov = random.randint(1, 10)

    if 1 <= mov <= 5:
        print("Passo veloce")
        posizione_tart += 3 
        
    elif 6 <= mov <= 7:
        print("Scivolata")
        posizione_tart -= 6

    elif 8 <= mov <= 10:
        print("Passo lento")
        posizione_tart += 1
    
    if posizione_tart < 1:
        posizione_tart = 1
        
    return posizione_tart


def mossa_lepre(posizione_lepre:int):
    mov = random.randint(1, 10)

    if 1 <= mov <= 2:
        print("Non si muove")
        
    elif 3 <= mov <= 4:
        print("Grande balzo")
        posizione_lepre += 9

    elif mov == 5:
        print("Grande scivolata")
        posizione_lepre -= 12
        
    elif 6 <= mov <= 8:
        print("Piccolo balzo")
        posizione_lepre += 1
        
    elif 9 <= mov <= 10:
        print("Piccola scivolata")
        posizione_lepre -= 2

    if posizione_lepre < 1:
        posizione_lepre = 1
    
    return posizione_lepre

def gara():
    posizione_tarta = 0
    posizione_lepre = 0

    print("'BANG !!!!! AND THEY'RE OFF !!!!!'")

    while posizione_tarta < 70 and posizione_lepre < 70: # qui simulo il movimento finchè nessuno dei due vince

        posizione_tarta = mossa_tartaruga(posizione_tarta) #123
        posizione_lepre = mossa_lepre(posizione_lepre)

        percorso(posizione_tarta, posizione_lepre) # stampo lo stato del percorso (richiamo la funzione def percorso ())
        
        if posizione_lepre >= 70 and posizione_tarta >= 70:
            print("IT'S A TIE.")
            return

        elif posizione_tarta >= 70:
            print("TORTOISE WINS! || VAY!!!")
            return
        
        elif posizione_lepre >=70:
            print("HARE WINS || YUCH!!!")
            return

gara()
    















#123     -> In queste righe, stiamo aggiornando le posizioni di entrambi gli animali (la tartaruga e la lepre) 
# ogni volta che vengono eseguite. Queste funzioni determinano come si spostano gli animali (ad esempio, avanzano 
# di una certa quantità o retrocedono) a seconda dei numeri casuali generati.



