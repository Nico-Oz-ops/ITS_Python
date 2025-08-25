'''
Raggruppa parole per lunghezza

Tema: Liste e dizionari
Obiettivo: Raggruppare stringhe in base alla loro lunghezza

Nome: raggruppa_per_lunghezza

Traccia:
Scrivi una funzione raggruppa_per_lunghezza(parole: list[str]) -> dict[int, list[str]] 
che ritorni un dizionario dove le chiavi sono le lunghezze e i valori le parole di quella lunghezza.

Input:
parole = ["ciao", "python", "java", "ok", "esercizio", "test"]
'''
def raggruppa_per_lunghezza(parole: list[str]) -> dict[int, list[str]]:
    risultato = {}
    
    for parola in parole:
        len_parola = len(parola)
        if len_parola not in risultato:
            risultato[len_parola] = []
        
        risultato[len_parola].append(parola)
    
    risultato_ordinato = dict(sorted(risultato.items()))
    return risultato_ordinato

parole = ["ciao", "python", "java", "ok", "esercizio", "test"]
print(raggruppa_per_lunghezza(parole))