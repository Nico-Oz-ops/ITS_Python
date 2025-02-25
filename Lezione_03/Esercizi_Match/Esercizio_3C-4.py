animale = input("Inserire il nome di un animale: ")

mammiferi = ["cane", "gatto", "cavallo", "elefante", "leone"]
rettili = ["serpente", "lucertola", "tartaruga", "coccodrillo"]
uccelli = ["aquila", "pappagallo", "gufo", "falco"]
pesci = ["squalo", "trota", "salmone", "carpa"]

match animale:
    case animale if animale in mammiferi:
        print(f"Il \"{animale}\" è un mammifero")
    case animale if animale in rettili:
        print(f"Il \"{animale}\" è un rettile")
    case animale if animale in uccelli:
        print(f"Il \"{animale}\" è un uccello")
    case animale if animale in pesci:
        print(f"Il \"{animale}\" è un pesce")
    case _:
        print(f"Non so dire in quale categoria classificare l'animale \"{animale}\"")