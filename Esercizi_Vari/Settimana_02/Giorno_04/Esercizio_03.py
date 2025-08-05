'''
Tema: Ricorsione + stringhe
Obiettivo: Verificare se in una stringa ci sono due lettere uguali consecutive (es. "palla" ha le doppie ll).
'''

# Esercizio 03
# Titolo: "Doppie consecutive"

'''
Traccia:
Scrivi una funzione ricorsiva ha_doppie(s: str) -> bool che restituisce True se la 
stringa contiene almeno una coppia di lettere consecutive uguali, altrimenti False.

Suggerimento (se ti serve):
Confronta s[0] con s[1], poi richiama la funzione sulla sottostringa s[1:].
'''

def ha_doppie(s: str) -> bool:

    if len(s) < 2:
        return False 
    
    if s[0] == s[1]:
        return True
    
    else:
        return ha_doppie(s[1:])

print(ha_doppie("llovido"))
print(ha_doppie("paralelepipedo"))
print(ha_doppie("pizza"))
    