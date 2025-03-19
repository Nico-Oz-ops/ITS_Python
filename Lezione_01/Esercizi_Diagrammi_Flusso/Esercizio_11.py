# Esercizio 11 - Sistema di prenotazione di posti

sedie_libere = 20

# Uso di ciclo while
while True:
    opzione = input("Scegliere una delle seguenti opzioni: \"prenota\", \"libera\", \"visualizza\" o \"esci\": ").lower()

    if opzione == "prenota":
        if sedie_libere > 0:
            sedie_libere -= 1
            print("Prenotazione avvenuta con successo!")
        else:
            print("Non ci sono posti liberi :/")

    elif opzione == "libera":
        if sedie_libere < 20:
            sedie_libere += 1
            print("Posto liberato con successo!")
        else:
            print("Tutti i posti sono disponibili")

    elif opzione == "visualizza":
        print(f"Ci sono {sedie_libere} sedie libere")
        print(f"Ci sono {20 - sedie_libere} sedie prenotate")

    elif opzione == "esci":
        print("A presto :) !")
        break

    else:
        print("Opzione non valida, per favore scegliere tra: \"prenota\", \"libera\", \"visualizza\" o \"esci\"")


# Uso di match statement
while True:
    opzione = input("\nScegliere una delle seguenti opzioni: \"prenota\", \"libera\", \"visualizza\" o \"esci\": ").lower()

    match opzione:
        case "prenota":
            if sedie_libere > 0:
                sedie_libere -= 1
                print("\nPrenotazione avvenuta con successo!")
            else:
                print("\nNon ci sono posti liberi!")
        case "libera":
            if sedie_libere < 20:
                sedie_libere += 1
                print("\nPosto liberato con successo!")
            else:
                print("\nTutti i posti sono disponibili!")
        case "visualizza":
            print(f"\nCi sono {sedie_libere} sedie libere.")
            print(f"\nCi sono {20 - sedie_libere} sedie prenotate.")
        case "esci":
            print("\nA presto!")
            break
        case _:
            print("\nOpzione non valida, per favore scegliere tra: \"prenota\", \"libera\", \"visualizza\" o \"esci\".")
            
       





