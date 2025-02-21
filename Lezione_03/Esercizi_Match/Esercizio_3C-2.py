voto_laurea = int(input("Inserire un voto compreso tra 66 e 110: "))

match voto_laurea:
    case voto_laurea if voto_laurea >= 106 and voto_laurea <= 110:
        print(f"Il tuo voto di laurea è {voto_laurea}, cioè GPA 4.0")
    case voto_laurea if voto_laurea >= 101 and voto_laurea <= 105:
        print(f"Il tuo voto di laurea è {voto_laurea}, cioè GPA 3.7")
    case voto_laurea if voto_laurea >= 96 and voto_laurea <= 100:
        print(f"Il tuo voto di laurea è {voto_laurea}, cioè GPA 3.3")
    case voto_laurea if voto_laurea >= 91 and voto_laurea <= 95:
        print(f"Il tuo voto di laurea è {voto_laurea}, cioè GPA 3.0")
    case voto_laurea if voto_laurea >= 86 and voto_laurea <= 90:
        print(f"Il tuo voto di laurea è {voto_laurea}, cioè GPA 2.7")
    case voto_laurea if voto_laurea >= 81 and voto_laurea <= 85:
        print(f"Il tuo voto di laurea è {voto_laurea}, cioè GPA 2.3")
    case voto_laurea if voto_laurea >= 76 and voto_laurea <= 80:
        print(f"Il tuo voto di laurea è {voto_laurea}, cioè GPA 2.0")
    case voto_laurea if voto_laurea >= 70 and voto_laurea <= 75:
        print(f"Il tuo voto di laurea è {voto_laurea}, cioè GPA 1.7")
    case voto_laurea if voto_laurea >= 66 and voto_laurea <= 69:
        print(f"Il tuo voto di laurea è {voto_laurea}, cioè GPA 1.0")
    case _:
        print("Voto non valido")