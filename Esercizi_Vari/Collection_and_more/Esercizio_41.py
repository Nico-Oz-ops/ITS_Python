'''
Tema: Liste e dizionari
Obiettivo: Separare elementi di tipi diversi presenti in una lista e organizzarli in un dizionario

Nome dell’esercizio: raggruppa_numeri_parole

Traccia:
Scrivi una funzione raggruppa_numeri_parole(lista: list) che, 
data una lista contenente numeri e parole, ritorni un dizionario con due chiavi:

"numeri" → lista contenente tutti gli elementi di tipo numerico presenti nella lista

"parole" → lista contenente tutti gli elementi di tipo stringa presenti nella lista

Esempio:
input: [1, "ciao", 3, "python", 7]
output: {"numeri": [1, 3, 7], "parole": ["ciao", "python"]}

Suggerimento:
Puoi usare un ciclo for per scorrere la lista e la funzione isinstance() per distinguere numeri e stringhe.
'''
from typing import Any

def raggruppa_numeri_parole(lista: list[Any]) -> dict[str, list[Any]]:
    risultato = {"numeri": [], "parole": []}

    for elemento in lista:
        if isinstance(elemento, (int, float)):
            risultato["numeri"].append(elemento)

        elif isinstance(elemento, str):
            risultato["parole"].append(elemento)
    
    return risultato

lista = [1, "ciao", 3, "python", 7, 2.35]
print(raggruppa_numeri_parole(lista))
