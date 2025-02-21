neonato = int(input("Inserisci il numero di neonati: "))

match neonato:
    case 1:
        print("Congratulazione")
    case 2:
        print("Gemelli")
    case 3:
        print("Wow tre!")
    case 4:
        print("Mamma mia quattro!")
    case 5:
        print("Incredibile, cinque!")
    case _:
        print(f"Non ci credo {neonato} bambini!")
        