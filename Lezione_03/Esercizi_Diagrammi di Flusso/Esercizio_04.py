# Esercizio 4 - Assegnazione di un tutor

tutor = 10
attesa = 0

while True:

    studente = input("Inserisci il tuo nome: ").lower()

    if tutor > 0:
        tutor -= 1
        print("Tutor assegnato con successo")
    else:
        attesa += 1
        print("Studente in attesa")
    
    if tutor == 0 and attesa > 20:
        print("La lista d'attesa è piena e non ci sono tutor disponibili")
        break


    

    