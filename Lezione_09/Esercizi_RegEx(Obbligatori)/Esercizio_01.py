# Esercizio 01
'''
Riconoscere numeri
Obiettivo: Definire una RegEx che riconosca solo stringhe composte da cifre.

Esercizio 1.1: Scrivi una RegEx che riconosca un numero intero positivo (es. 123, 98765).
Esercizio 1.2: Modifica la RegEx per accettare anche numeri negativi (es. -45, -1000, 0).
'''

import re

# Esercizio 1.1
stringa:list = ["275", "27gf", "15a", "2", "123abc", "-1225"]
pattern = r"\d+"

numeri_interi_positivi = [num for num in stringa if re.fullmatch(pattern, num)]
print(numeri_interi_positivi)

txt:str = "Nico ha 234 anni e 3 cani"
numeri_positivi = re.findall(r"\d+", txt)
print(numeri_positivi)

num_posi = ^\d+$

# Esercizio 1.2
txt:str = "Nico ha 234 anni e 3 cani e -3 gatti"
numeri_positivi = re.findall(r"-?\d+", txt)
print(numeri_positivi)

num = ^-?\d+$

