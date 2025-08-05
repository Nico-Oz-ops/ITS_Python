'''
Obiettivo: 
Allenarti a:
* usare i cicli per scorrere stringhe
* applicare condizioni
* usare str.lower() per uniformare il testo
'''

# Esercizio 04
# Titolo: "Conta le vocali"

'''
Traccia:
Scrivi una funzione chiamata conta_vocali() che:

* Chiede all’utente di inserire una frase
* Conta quante vocali contiene la frase (a, e, i, o, u)
* Ignora maiuscole e spazi
* Stampa il numero totale di vocali trovate

Suggerimenti:
* Usa input().lower() per semplificare il confronto
* Puoi usare 'in' per verificare se un carattere è in una lista/insieme: "aeiou"
'''

def conta_vocali():
    
    input_frase = input("Inserire una frase: ").lower().strip()

    vocali = 0

    for lettera in input_frase:
        if lettera in "aeiou":
            vocali += 1
    return f"La frase '{input_frase}' contiene: {vocali} vocali"

print(conta_vocali())

