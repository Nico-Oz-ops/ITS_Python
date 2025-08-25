'''
Conta vocali e consonanti

Tema: Dizionari e stringhe
Obiettivo: Contare quante vocali e consonanti ci sono in una stringa

Nome: conteggio_vocali_consonanti

Traccia:
Scrivi una funzione conteggio_vocali_consonanti(testo: str) -> dict[str, int] 
che ritorni un dizionario con chiavi "vocali" e "consonanti" e valori il 
numero di ciascuno, ignorando spazi e punteggiatura.

Input:
testo = "Python è fantastico"
'''
def conteggio_vocali_consonanti(testo: str) -> dict[str, int]:
    risultato = {"vocali": 0, "consonanti": 0}

    for cararattere in testo:
        if cararattere.isalpha():
            car = cararattere.lower()
            if car in "aeiou":
                risultato["vocali"] += 1
            else:
                risultato["consonanti"] += 1

    return risultato

testo = "Python è fantastico"
print(conteggio_vocali_consonanti(testo))
