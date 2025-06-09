# Esercizio 02
'''
Trova le vocali e salvale in una lista

Hai una stringa. Crea un ciclo che esamina ogni lettera e salva solo le vocali in una lista.
Scrivi un codice che:

    *prende una stringa,

    *controlla ogni carattere,

    *se è una vocale (a, e, i, o, u), la aggiunge a una lista.
'''

stringa = "Hola mUNdo!"
solo_vocali = []

for lettera in stringa:

    if lettera.lower() in "aeiou":
        solo_vocali.append(lettera)
    
print(solo_vocali)

def trova_vocali(stringa: str) -> list[str]:
    vocali = []

    for carattere in stringa:
        if carattere.lower() in "aeiou":
            vocali.append(carattere)
    
    return vocali

mystring = "Paralelepipedo"
print(trova_vocali(mystring))




