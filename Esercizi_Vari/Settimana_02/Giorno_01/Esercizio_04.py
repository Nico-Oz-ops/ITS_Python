'''
Tema: Funzioni ricorsive
Obiettivo: Usare la ricorsione per invertire una stringa carattere per carattere.
'''

# Esercizio 04
# Titolo: "Parola al Contrario"

'''
Traccia:
Scrivi una funzione ricorsiva chiamata inverti_parola(parola: str) -> str 
che riceve una stringa e la restituisce invertita, senza usare slicing ([::-1]) 
né funzioni come reversed() o cicli (for, while).

Suggerimento (se ti serve):
Pensa a come puoi prendere il primo carattere e metterlo 
alla fine della parola invertita del resto.
'''

def inverti_parola(parola: str) -> str:
    if len(parola) <= 1:
        return parola 
    
    else:
        return inverti_parola(parola[1:]) + parola[0]

print(inverti_parola("hola gente, CòmO eStàN?"))
    


# opzione con slicing

def inverti_parola_2(parola: str) -> str:
    return parola[::-1]
print(inverti_parola_2("hola"))

# opzione con ciclo for
def inverti_parola_3(parola: str) -> str:

    parola_inv = ""

    for car in parola:
        parola_inv = car + parola_inv

    return parola_inv
print(inverti_parola_3("holasasaA"))

# opzione ciclo while
def inverti_parola_4(parola: str) -> str:
    
    parola_inv = ""
    i = len(parola) - 1

    while i >= 0:
        parola_inv += parola[i]

        i -= 1
    return parola_inv
print(inverti_parola_4("hola gente"))

# opzione reversed()
def inverti_parola_5(parola: str) -> str:
    return reversed(parola)
print(inverti_parola("adios a todos"))


