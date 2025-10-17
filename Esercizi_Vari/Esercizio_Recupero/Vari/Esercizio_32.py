'''
Tema: Dizionari - Raggruppamento di dati
Obiettivo: Costruire un dizionario a partire da una lista, 
organizzando gli elementi secondo una logica specifica.

Nome dell’esercizio: Raggruppa parole per lunghezza

Traccia:
Scrivi una funzione raggruppa_parole(parole: list[str]) -> dict[int, list[str]] che, 
dato un elenco di parole, le raggruppi in un dizionario in base alla loro lunghezza.

La chiave del dizionario deve essere la lunghezza della parola, e il valore deve essere 
la lista delle parole di quella lunghezza.

Esempio input:
parole = ["cane", "gatto", "sole", "luna", "amico", "io", "tu", "computer"]

Suggerimento:
Puoi scorrere la lista parola per parola, calcolare la lunghezza e inserire la parola 
nella lista corrispondente nel dizionario. Se la chiave non esiste ancora, devi crearla.
'''

# Alternativa 1
def ragruppa_parole(parole: list[str]) -> dict[int, list[str]]:

    dict_parole = {}

    for parola in parole:
        len_parola = len(parola)
        if len_parola not in dict_parole:
            dict_parole[len_parola] = []
        
        dict_parole[len_parola].append(parola)
    
    risultato_ordinato = dict(sorted(dict_parole.items()))
    return risultato_ordinato

parole = ["cane", "gatto", "sole", "luna", "amico", "io", "tu", "computer"]
print(ragruppa_parole(parole))

# Alternativa 2
# def ragruppa_parole(parole: list[str]) -> dict[int, list[str]]:

#     dict_parole = {}

#     for parola in parole:
#         len_parola = len(parola)
#         if len_parola not in dict_parole:
#             dict_parole[len_parola] = []
        
#         dict_parole[len_parola].append(parola)
    
#     n = list(dict_parole.keys())
#     len_n = len(n)

#     for i in range(len_n):
#         for j in range(0, len_n - i - 1):
#             if n[j] > n[j + 1]:



#     return dict_parole

# parole = ["cane", "gatto", "sole", "luna", "amico", "io", "tu", "computer"]
# print(ragruppa_parole(parole))
