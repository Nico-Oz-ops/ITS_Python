voto = int(input("Inserire un voto: "))

match voto:
    case 10:
        print("Eccellente")
    case voto if voto >= 8 and voto < 10:
        print("Molto buono")
    case voto if voto >= 6 and voto < 8:
        print("Sufficiente")
    case voto if voto >= 4 and voto < 6:
        print("Insufficiente")
    case voto if voto > 0 and voto < 4:
        print("Gravemente insufficiente")
    case _:
        print("Voto non valido")