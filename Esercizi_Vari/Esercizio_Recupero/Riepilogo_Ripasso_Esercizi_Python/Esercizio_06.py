'''
Scrivi una funzione che accetti tre parametri: username, password e status di attivazione 
dell'account (attivo/non attivo). L'accesso è consentito solo se il nome utente è "admin", 
la password corrisponde a "12345" e l'account è attivo. La funzione ritorna "Accesso consentito" 
oppure "Accesso negato".

For example:

Test:
print(check_access("admin", "12345", True))
Accesso consentito

print(check_access("admin", "54321", True))
Accesso negato
'''
from typing import Any

def check_access(username: str, password: Any, is_active: bool) -> str:
    if username == "admin" and password == "12345" and is_active:
        return "Accesso consentito"
    else:
        return "Accesso negato"

print(check_access("admin", "12345", True))
print(check_access("admin", "54321", True))