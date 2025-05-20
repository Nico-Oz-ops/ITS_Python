# Esercizio 2

import re

def extract_emails(text:str):

    return re.findall(r"\S+@\S+", text)

text = "Contattaci a info@azienda.com oppure support@help.org"
print(extract_emails(text))