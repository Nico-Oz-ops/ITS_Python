'''
Tema: Condizioni + input + logica base
Obiettivo: Allenarti con condizioni composte usando if, elif, else e l’operatore % (modulo).
'''

# Esercizio 01
# Titolo: "Multiplo di 3 e 5"

'''
Scrivi una funzione multiplo_3_5() che:

Chiede all’utente di inserire un numero intero

Verifica se è:

Multiplo di 3 e 5 → stampa "Multiplo di 3 e 5"

Solo di 3 → stampa "Multiplo di 3"

Solo di 5 → stampa "Multiplo di 5"
'''

def multiplo_3_5():

    try:
        input_num = int(input("Inserire un numero intero: "))

    except ValueError:
        return "Errore, il numero inserito non è intero."
    
    if input_num % 3 == 0 and input_num % 5 == 0:
        return f"'{input_num}' è multiplo di 3 e 5"
    
    elif input_num % 3 == 0:
        return f"'{input_num}' è multiplo di 3"
    
    elif input_num % 5 == 0:
        return f"'{input_num}' è multiplo di 5"
    
    else:
        return f"'{input_num}' non è multiplo di 3 néd di 5"

print(multiplo_3_5())



