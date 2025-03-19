# Esercizio 01 - Sistema di gestione per un parcheggio

max_posti = int(input("\nInserire il numero massimo di posti: "))
liberi = max_posti

# Uso ciclo while/if/elif/else

while True:
    opzione = input("\nInserire una delle seguenti opzioni: \"ingresso\", \"uscita\", \"stato\", \"esci\": ").lower()

    if opzione == "ingresso":
        if liberi > 0:
            liberi -= 1
            print("\nHai occupato un posto")
        else:
            print("\nNon ci sono posti disponibili")

    elif opzione == "uscita":
        if liberi < max_posti:
            liberi += 1
            print("\nPosto liberato")
        else:
            print("\nTutti i posti sono già disponibili")
    
    elif opzione == "stato":
        print(f"\nCi sono {liberi} posti liberi.")
        print(f"\nCi sono {max_posti - liberi} posti occupati")
    
    elif opzione == "esci":
        print("\nA presto!")
        break

    else:
        print("\nOpzione non valida. Inserire una delle seguenti opzioni: \"ingresso\", \"uscita\", \"stato\", \"esci\"")


# Opzione uso match statement

max_posti = int(input("\nInserire il numero massimo di posti: "))
liberi = max_posti

while True:
    opzione = input("\nInserire una delle seguenti opzioni: \"ingresso\", \"uscita\", \"stato\", \"esci\": ").lower()

    match opzione:
        case "ingresso":
            if liberi > 0:
                liberi -= 1
                print("\nHai occupato un posto")
            else:
                print("\nNon ci sono posti disponibili")

        case "uscita":
            if liberi < max_posti:
                liberi += 1
                print("\nPosto liberato")
            else:
                print("\nTutti i posti sono già disponibili")
    
        case "stato":
            print(f"\nCi sono {liberi} posti liberi.")
            print(f"\nCi sono {max_posti - liberi} posti occupati")
    
        case "esci":
            print("\nA presto!")
            break

        case _:
            print("\nOpzione non valida. Inserire una delle seguenti opzioni: \"ingresso\", \"uscita\", \"stato\", \"esci\"")

