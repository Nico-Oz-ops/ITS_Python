'''
Obiettivo: Allenarti con:
* while True
* input()
* condizioni multiple (len, any, isalpha, isdigit)
'''

# Esercizio 05
# Titolo: Password sicura"

'''
Traccia:
Scrivi una funzione richiedi_password() che:

Chiede all’utente di inserire una password.

Continua a chiedere finché non rispetta tutte le condizioni:

* Deve contenere almeno 8 caratteri
* Deve contenere almeno una lettera
* Deve contenere almeno un numero

Quando la password è valida:

* Stampa "Password accettata"
* Ritorna la password
'''

def richiedi_password() -> str:

    while True:
        input_password = input("Inserire la password: ")

        if len(input_password) >= 8 and \
        any(car.isalpha() for car in input_password) and \
        any(car.isdigit() for car in input_password):
            print("Password accettata")
            return input_password

        else:
            print(f"Password '{input_password}' non accettata. La password deve contenere 8 caratteri, almeno una lettera e un numero")

password = richiedi_password()
print(f"Password scelta: {password}")

