# Classificare un mese
mese = input("Inserire un mese: ").lower()

# Opzione 1
stagioni = {
    "inverno": ["dicembre", "gennaio", "febbraio"],
    "primavera": ["marzo", "aprile", "maggio"],
    "estate": ["giugno", "luglio", "agosto"],
    "autunno": ["settembre", "ottobre", "novembre"],
}

match mese:
    case mese if mese in stagioni["inverno"]:
        print("inverno")
    case mese if mese in stagioni["primavera"]:
        print("primavera")
    case mese if mese in stagioni["estate"]:
        print("estate")
    case mese if mese in stagioni["autunno"]:
        print("autunno")
    case _:
        print(f"{mese} non riconosciuto")


# Opzione 2
match mese:
    case "dicembre"|"gennaio"|"febbraio":
        print("inverno")
    case "marzo"|"aprile"|"maggio":
        print("primavera")
    case "giugno"|"luglio"|"agosto":
        print("estate")
    case "settembre"|"ottobre"|"novembre":
        print("autunno")
    case _:
        print(f"{mese} non riconosciuto")