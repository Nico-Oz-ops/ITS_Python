nome = input("Inserire il tuo nome: ")
genere = input("Inserire il tuo genere (\"m\" per maschio e \"f\" per femmina): ")

match (genere, nome):
    case ("m", nome):
        print(f"Nome: {nome}\nGenere: Maschio")
    case ("f", nome):
        print(f"Nome: {nome}\nGenere: Femmina")
    case _:
        print(f"Mi dispiace {nome} non è possibile generare un documento di identità per te")