# Esercizio 1
'''
Indovinare un numero intero in cui il computer pensa a
un numero e il giocatore ha diverse possibilità di indovinarlo, non è necessario continuare a
chiedere al giocatore dopo che ha indovinato correttamente. Il giocatore ha 5 tentativi per indovinare il numero,
altrimento perde il gioco
'''

numero_da_indovinare = 69
numero_indovinato = False

for tentativo in range(1, 5 + 1):

    while True:
        num = input("\nIndovina il numero. Inserisci un numero intero: ")

        if num.lstrip("-").isdigit():
            num = int(num)
            break
        else:
            print("\nErrore. Prova ad inserire un numero intero")

    if num == numero_da_indovinare:
        numero_indovinato = True
        break

    else:
        print(f"\nNumero non indovinato, hai ancora {5 - tentativo} tentativi")

messaggio = "\nHai vinto! Hai indovinato il numero!" if numero_indovinato else "\nHai perso! Mi dispiace :/"

print(messaggio)

