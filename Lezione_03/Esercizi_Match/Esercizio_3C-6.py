animale = input("Inserire il nome di un animale: ").lower()
habitat = input("Inserire l'habitat in cui vive l'animale (acqua, terra, aria): ").lower()

mammiferi = ["cane", "gatto", "cavallo", "elefante", "leone", "balena", "delfino"]
rettili = ["serpente", "lucertola", "tartaruga", "coccodrillo"]
uccelli = ["aquila", "pappagallo", "gufo", "falco", "cigno", "anatra", "gallina", "tacchino"]
pesci = ["squalo", "trota", "salmone", "carpa"]

animal_type = "unknown"


match animale:
    case animale if animale in mammiferi:
        animal_type = "mammifero"
        print(f"Il \"{animale}\" è un mammifero")   
    case animale if animale in rettili:
        animal_type = "rettile"
        print(f"Il \"{animale}\" è un rettile")
    case animale if animale in uccelli:
        animal_type = "uccello"
        print(f"Il \"{animale}\" è un uccello")
    case animale if animale in pesci:
        animal_type = "pesce"
        print(f"Il \"{animale}\" è un pesce")
    case _:
        animal_type = "unknown"
        print(f"Non so dire in quale categoria classificare l'animale \"{animale}\"")



info_animale = {
    "nome": animale,
    "tipo animale": animal_type,
    "habitat": habitat,
}

match (animal_type, habitat ):
    case ("mammifero", "terra"):
        print(f"L'animale {animale} può viere sulla terra")
    case ("rettile", "terra"):
        print(f"L'animale {animale} può viere sulla terra")
    case ("mammifero", "acqua"):
        print(f"L'animale {animale} può viere sulla acqua")
    case ("rettile", "acqua"):
        print(f"L'animale {animale} può viere nell'acqua")
    case ("uccello", "terra"):
        print(f"L'animale {animale} può viere sulla terra")
    case ("uccello", "aria"):
        print(f"L'animale {animale} può viere nell'aria")