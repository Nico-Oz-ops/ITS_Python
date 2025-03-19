# Esercizio 8.13 - Profilo utente

# Opzione 1 - stringa formattata
# def build_profile(myname:str, myage:int, myhair:str, myweight:int):
#     return f"{myname}, {myage} anni, capelli {myhair}, {myweight}kg"
# info_usuario = build_profile("Nicolas Valenzuela", 36, "oscuri", 70)

# print(info_usuario)

# Opzione 2 - dizionario
# def build_profile(myname:str, myage:int, myhair:str, myweight:int):
#     profilo_personale = {"nome_cognome": myname, "età": myage, "colore_capelli": myhair, "peso": myweight}
#     return profilo_personale

# info_usuario = build_profile("Nicolas Valenzuela", 36, "oscuri", 70)

# print(f"Nome e Cognome: {info_usuario['nome_cognome']}")
# print(f"Età: {info_usuario['età']} anni")
# print(f"Capelli: {info_usuario['colore_capelli']}")
# print(f"Peso: {info_usuario['peso']}kg")

# Opzione 3 - kwargs
def build_personale (nome: str, cognome:str, **kwargs):

    profilo = f"{nome} {cognome}"

    for key, value in kwargs.items():
        profilo += f", {key}: {value}"
    return profilo
      
info_utente = build_personale("Nico", "Valenzuela", genere="maschile", etnia="ununaki", città="Roma")
print(info_utente)


