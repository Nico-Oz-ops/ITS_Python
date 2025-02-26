frase = input("Scrivi una frase: ")

ultimo_carattere = frase[-1]

match ultimo_carattere:
    case "?" if len(frase) % 2 == 0:
        print("Sì")
    case "?" if len(frase) % 2 != 0:
        print("No")
    case "!":
        print("Wow!")
    case _:
        print(f"Tu dici \"{frase}\"")
            