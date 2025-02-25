name = input("Inserire il nome dell'utente: ")
ruolo = input("Inserire il ruolo dell'utente: ")
età = int(input("Inserire l'età dell'utente: "))

dict_user = {
    "nome": name,
    "ruolo": ruolo,
    "età": età,
}

match dict_user:
    case {"nome": name, "ruolo": "admin"}:
        print(f"Salve {name}, hai accesso completio a tutte le funzionalità")
    case {"nome": name, "ruolo": "moderatore"}:
        print(f"Salve {name}, può gestire i contenuti ma non modificare le impostazioni")
    case {"nome": name, "ruolo": "utente adulto", "età": età} if età >= 18:
        print(f"Salve {name}, ha accesso standard a tutti i servizi")
    case {"nome": name, "ruolo": "utente minorenne", "età": età} if età < 18:
        print(f"Ciao! {name} hai accesso limitato! Alcune funzionalità sono bloccate")
    case {"nome": name, "ruolo": "ospite"}:
        print(f"Salve {name}, hai accesso ristretto. Solo visualizzazione dei contenuti" )
    case _:
        print(f"Ciao {name}! Attenzione! Ruolo non riconosciuto! Accesso negato!")