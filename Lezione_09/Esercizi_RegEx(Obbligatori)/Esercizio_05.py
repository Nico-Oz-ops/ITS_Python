# Esercizio 5

'''
Riconoscere date
Obiettivo: Lavorare con formati numerici separati da caratteri speciali.

Esercizio 5.1: Scrivi una RegEx che riconosca una data nel formato gg/mm/aaaa (es. 09/04/2025).
Esercizio 5.2: Adatta la RegEx per accettare anche il formato gg-mm-aaaa.
'''

# Esercizio 5.1
data (gg/mm/aaaa) = ^\d{2}/\d{2}/\d{4}$

# Esercizio 5.2
data = ^\d{2}\-\d{2}\-\d{4}$
data = ^\d{2}-\d{2}-\d{4}$