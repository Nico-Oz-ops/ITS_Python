oggetti = [] 

for oggetto in range(3):
    oggetti.append(input("Inserire un oggetto: "))
    print(oggetti)

match oggetti:
    case ["quaderno", "penna", "matita"]:
        print("Materiale scolastico")
    case ["pane", "latte", "uova"]:
        print("Prodotti alimentari")
    case ["sedia", "tavolo", "armadio"]:
        print("Mobili")
    case ["telefono", "computer", "tablet"]:
        print("Dispositivi elettronici")
    case _:
        print("Categoria sconosciuta")