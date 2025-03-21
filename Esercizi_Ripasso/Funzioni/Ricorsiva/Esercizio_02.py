# Esercizio 2 - Countdown

def countdown(num:int) -> None:
    if num < 0:
        print("Errore")
    
    elif num == 0:
        print(0) 
    
    else:
        print(num)
        countdown(num - 1)
    
countdown(5)