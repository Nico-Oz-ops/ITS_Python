'''
Obiettivo: Allenare if, elif, else con un controllo numerico semplice.
'''

# Esercizio 02
# Titolo: Numero positivo, negativo o zero"

'''
Traccia:
Scrivi una funzione analizza_numero() che:

Chieda all’utente un numero (anche negativo).

Restituisca:

"Positivo" se il numero è maggiore di zero.

"Negativo" se è minore di zero.

"Zero" se è uguale a zero.
'''

def analizza_numero() -> str:
    input_num = int(input("Inserire un qualsiasi numero intero: "))

    if input_num > 0:
        return "Positivo"
    elif input_num < 0:
        return "Negativo"
    else:
        return "Zero"

print(analizza_numero())