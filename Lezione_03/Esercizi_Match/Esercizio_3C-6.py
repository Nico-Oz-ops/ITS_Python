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

match info_animale:
    case info_animale if habitat in ["terra", "acqua"]:
        match animale:
            case animale if animale in ["cane", "gatto", "cavallo", "elefante", "leone"] and habitat == "terra":
                print(f"L'animale {animale} è uno dei mamiferi che può vivere sulla terra")
            case animale if animale in ["balena", "delfino"] and habitat == "acqua":
                print(f"L'animale {animale} è uno dei mamiferi che può vivere sull'acqua")
            case _: 
                print(f"Non ho mai visto l'animale {animale} vivere nell'habitat {habitat}")
                
