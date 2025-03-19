# Eserciziuo 01 - Sistem,a che gestisce comandi utente

comando_utente = input("Inserire un comando tra le seguenti opzioni: \"avvia\", \"arresta\", \"pausa\", \"stato\": ")

match comando_utente:
    case "avvia":
        print("Il sistema deve avviare una procedura.")
    case "arresta":
        print("Il sistema deve fermare una procedura.")
    case "pausa":
        print("Il sistema deve mettere una procedura in pausa.")
    case "stato":
        print("Il sistema deve mostrare lo stato corrente.")
    case _: 
        print("Errore, comando non valido.")