# Esercizio 2
'''
Riconoscere parole
Obiettivo: Lavorare con lettere e lunghezze di stringhe.

Esercizio 2.1: Scrivi una RegEx che riconosca una parola composta solo da lettere minuscole.
Esercizio 2.2: Adatta la RegEx per accettare parole con lettere maiuscole e minuscole.
Esercizio 2.3: Modifica la RegEx per accettare parole lunghe da 5 a 10 caratteri.
'''

import re
# Esercizio 2.1
txt:str = "nico, Lisa, cachina, morbida, marEmma"
result = re.findall(r'\b[a-z]+\b', txt)
print(result)

txt:str = "coni"
result = re.findall(r'^[a-z]+$', txt)
# print(result)

# Esercizio 2.2
txt:str = "Santiago"
result = re.findall(r"[A-Z][a-z]+", txt)
print(result)

# Esercizio 2.3
txt1:str = "coccodrillo juancho ola"
result1 = re.findall(r'[a-zA-Z]{5,10}', txt1)
print(result1)

