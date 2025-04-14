# Esercizio 3
'''
Email semplici
Obiettivo: Definire pattern per email.

Esercizio 3.1: Scrivi una RegEx che riconosca email del tipo nome@dominio.com.
Esercizio 3.2: Estendi la RegEx per accettare anche domini con più estensioni, es. nome@dominio.co.uk.
'''

import re

# Esercizio 3.1
# email = "nvalenzuela@gmail.com"
# result:list[str] = re.findall(r"\S+@\S+", email)
# print(result)

email = "nvalenzuela@gmail.com"
pattern = ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$


# Esercizio 3.2
email = "nvalenzuela@dominio.co.uk"
pattern = ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})*$


