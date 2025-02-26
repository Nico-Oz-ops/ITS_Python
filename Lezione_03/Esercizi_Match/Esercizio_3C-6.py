animale = input("Inserire il nome di un animale: ").lower()
habitat = input("Inserire l'habitat in cui vive l'animale (acqua, terra, aria): ").lower()

mammiferi = ["cane", "gatto", "cavallo", "elefante", "leone", "balena", "delfino"]
rettili = ["serpente", "lucertola", "tartaruga", "coccodrillo"]
uccelli = ["aquila", "pappagallo", "gufo", "falco", "cigno", "anatra", "gallina", "tacchino"]
pesci = ["squalo", "trota", "salmone", "carpa"]

animal_type = "unknown"

habitat_corretto = {
    "mammifero": ["acqua", "terra"], #ci sono mammiferi che possono vivere in acqua e sulla terra
    "rettile": ["acqua", "terra"], #ci sono rettili che possono vivere in acqua e sulla terra
    "uccello": ["acqua", "terra", "aria"], #ci sono uccelli che possono vivere in acqua, sulla terra e in aria
    "pesce": ["acqua"] #i pesci solo vivono nell'acqua  
}

match animale:
    case animale if animale in mammiferi:
        animal_type = "mammifero"
        print(f"L'animale \"{animale}\" è un mammifero")   
    case animale if animale in rettili:
        animal_type = "rettile"
        print(f"L'animale \"{animale}\" è un rettile")
    case animale if animale in uccelli:
        animal_type = "uccello"
        print(f"L'animale \"{animale}\" è un uccello")
    case animale if animale in pesci:
        animal_type = "pesce"
        print(f"L'animale \"{animale}\" è un pesce")
    case _:
        animal_type = "unknown"
        print(f"Non so dire in quale categoria classificare l'animale \"{animale}\"")

info_animale = {
    "nome": animale,
    "tipo animale": animal_type,
    "habitat": habitat,
}

match (animal_type, habitat):
    case ("unknown", _):
        print(f"L'animale {animale} non è riconosciuto")
    case (_, habitat) if habitat not in ["acqua", "terra", "aria"]:
        print(f"{habitat} non è corretto")
    case (tipo, habitat) if habitat in habitat_corretto.get(tipo, []):
        print(f"L'habitat dell'animale {animale} è: {habitat}")
    case (tipo, habitat):
        if habitat in habitat_corretto[tipo]:
            print(f"L'animale {animale} può vivere in più habitat, persino {habitat}")
        else:
            print(f"L'animale {animale} di solito non vive un habitat come {habitat}")


        
# match info_animale:
#     case {"nome": animale, "habitat": habitat}:
#         print(f"L'animale {animale} solitamente vive in {habitat}")
#     case _:
#         print("Errore")
    