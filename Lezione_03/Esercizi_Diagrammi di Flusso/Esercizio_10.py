# Esercizio 10 - Validazione dell'età per l'attività

# Opzione base
# età_utente = int(input("Inserire la sua età: "))

# if età_utente >= 18 and età_utente <= 65:
#     print("Può partecipare all'attività")
    
# elif età_utente < 18:
#     print("Non può partecipare all'attività,\nperché non hai raggiunto l'età minima richiesta.")

# else:
#     print("Non può partecipare all'attività,\nperché ha superato l'età massima richiesta.")



# Opzione 2 - Uso di ciclo per controllare il valore dell'età (deve essere positivo e intero)
while True:    
    età_utente = input("Inserire la tua età: ")
    
    if età_utente.isdigit():
        età_utente = int(età_utente)
        if età_utente >= 0:
            break
        else:
            print("Errore, valore non valido. Riprova a inserire la tua età")
    else:
        print("Errore, valore non valido. Riprova a inserire la tua età")
    
if età_utente >= 18 and età_utente <= 65:
    print("Puoi partecipare all'attività")
        
elif età_utente < 18:
    print("Non può partecipare all'attività,\nperché non hai raggiunto l'età minima richiesta.")

else:
    print("Non può partecipare all'attività,\nperché hai superato l'età massima richiesta.")


