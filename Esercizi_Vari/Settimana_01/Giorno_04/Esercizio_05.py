'''
Tema: Condizioni multiple e contatori
Obiettivo:
Classificare una serie di età inserite dall’utente in tre gruppi:
* Minorenni (< 18 anni)
* Maggiorenni (18–64 anni)
* Anziani (65+ anni)
'''

# Esercizio 05
# Titolo: "Classifica età"

'''
Traccia:
Crea una funzione classifica_eta() -> None che:

Chiede all’utente di inserire età (numeri interi).
Termina l’inserimento quando l’utente scrive "stop".

Per ogni età valida:

* Se è < 18 → conta come minorenne
* Se è tra 18 e 64 (inclusi) → conta come maggiorenne
* Se è ≥ 65 → conta come anziano

Alla fine stampa:

* Numero totale di età inserite
* Quanti minorenni
* Quanti maggiorenni
* Quanti anziani

Suggerimento:
* Usa tre contatori separati (minorenni, maggiorenni, anziani)
* Ricorda di ignorare età negative con un messaggio di errore
'''

def classifica_eta() -> None:

    cont_totale_eta = 0
    cont_min = 0
    cont_mag = 0
    cont_anz = 0

    while True:
        input_eta = input("Inserire un età (oppure digitare 'stop' per terminare): ")

        if input_eta == "stop":
            break
            
        try:
            eta = int(input_eta)
            cont_totale_eta += 1

            if eta < 18:
                cont_min += 1

            elif 18 <= eta <= 64:
                cont_mag += 1

            else:
                cont_anz += 1

        except ValueError:
            print("Errore, l'età deve essere un numero intero")
    
    print(f"Numero totale di età inserite: {cont_totale_eta}")
    print(f"Numero di minorenni: {cont_min}")
    print(f"Numero di maggiorenni: {cont_mag}")
    print(f"Numero di anziani: {cont_anz}")

classifica_eta()

