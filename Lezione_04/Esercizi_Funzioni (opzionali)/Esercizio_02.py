# Esercizio 2
'''
Indovina il gioco dei numeri :

Creare una funzione che generi un numero casuale all'interno di un intervallo specificato dall'utente.
Richiedi all'utente di indovinare il numero entro un numero massimo di tentativi specificato.
Fornire un feedback all'utente dopo ogni tentativo, indicando se la sua tentazione è troppo alta, troppo bassa o corretta.
Termina il ciclo quando l'utente indovina il numero correttamente o raggiunge il numero massimo di tentativi.
'''

numero_indovinare = 8
numero_tentativi = 5
i = 1
while i <= numero_tentativi:
    chiede = int(input("Indovina il numero: "))

    if chiede == numero_indovinare:
        print("Complimenti hai indovinato")
        break
    
    else:
        numero_tentativi - 1 
        print(f"Non hai indovinato, hai ancora {numero_tentativi} tentativi")
        
