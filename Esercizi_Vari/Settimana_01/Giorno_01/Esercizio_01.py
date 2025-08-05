'''
Tema: Condizioni + input + logica base
Obiettivo: Allenare le condizioni if, elif, else e il ragionamento logico.
'''

# Esercizio 01
# Titolo: "Controllo età per l'accesso a un evento"

'''
Scrivi una funzione chiamata controlla_eta che:

Chieda all'utente la sua età (usando input()).

Stabilisca:

* Se l'età è minore di 14, stampa: "Accesso vietato."

* Se è tra 14 e 17, stampa: "Accesso con accompagnatore."

* Se è 18 o più, stampa: "Accesso consentito."
'''


def controlla_eta() -> str:
    input_eta = int(input("Quanti anni hai? "))

    if input_eta < 14:
        return "Accesso vietato"
    elif 14 <= input_eta <= 17:
        return "Accesso con accompagnatore"
    else:
        return "Accesso consentito"

print(controlla_eta())