'''
Tema: Cicli e condizioni
Obiettivo: Contare quante volte compaiono le lettere 'a', 'e' e 'z' in 
una stringa inserita dall’utente (ignorando maiuscole/minuscole).
'''

# Esercizio 03
# Titolo: "Conta lettere speciali"

'''
Traccia:
Scrivi una funzione conta_lettere_speciali() -> None che:

* Chieda all’utente di inserire una frase.
* Converta tutta la frase in minuscolo.
* Conti quante volte compaiono le lettere 'a', 'e' e 'z' nella frase.
* Stampi il risultato con un messaggio chiaro

Suggerimento (se serve):
Puoi usare .count("a") per contare quante volte una lettera appare in una stringa.
'''

def conta_lettere_speciali() -> None:

    cont_a = 0
    cont_e = 0
    cont_z = 0

    input_frase = input("Inserire una frase: ").strip().lower()

    for car in input_frase:
        if car == "a":
            cont_a += 1

        elif car == "e":
            cont_e += 1

        elif car == "z":
            cont_z += 1
    
    print(f"La lettera 'a' compare {cont_a} volte nella frase '{input_frase}'.")
    print(f"La lettera 'e' compare {cont_e} volte nella frase '{input_frase}'.")
    print(f"La lettera 'z' compare {cont_z} volte nella frase '{input_frase}'.")

conta_lettere_speciali()

# oppure

print("-------------------------------------------------------")

def conta_lettere_speciali() -> None:

    input_frase = input("Inserire una frase: ").strip().lower()

    lettera_a = input_frase.count("a")
    lettera_e = input_frase.count("e")
    lettera_z = input_frase.count("z")

    print(f"La lettera 'a' compare {lettera_a} volte nella frase '{input_frase}'.")
    print(f"La lettera 'e' compare {lettera_e} volte nella frase '{input_frase}'.")
    print(f"La lettera 'z' compare {lettera_z} volte nella frase '{input_frase}'.")

conta_lettere_speciali()





