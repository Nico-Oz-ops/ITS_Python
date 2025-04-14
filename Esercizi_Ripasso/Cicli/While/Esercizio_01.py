# Esercizio 1
'''
Indovinare un numero intero in cui il computer pensa a
un numero e il giocatore ha diverse possibilità di indovinarlo, non è necessario continuare a
chiedere al giocatore dopo che ha indovinato correttamente
'''

numero_da_indovinare = 71

while True:
    while True:
        num = input("\nInserire un numero intero: ")

        if num.lstrip("-").isdigit():
            num = int(num)
            break

        else:
            print("\nErrore. Prova a inserire un numero intero")
    
    if num == numero_da_indovinare:
        print("\nComplimenti, hai indovinato il numero!")
        break
    
    else:
        print("\nPeccato , numero non indovinato :(. Prova ad indovinare :)")


