# Esercizio 03 - Sistema di registrazione degli studenti a corsi

# corsi = {
#     "matematica": 100,
#     "informatica": 100,
#     "inglese": 100,
# }

# while True:
#     nome_corso = input("\nInserire il nome di un corso, tra informatica, matematica e inglese: ").lower()

#     if nome_corso not in corsi:
#         print("\nCorso non valido. Scegliere uno dei corsi tra le opzioni.")
#         continue

#     while True:
#         opzione = input("\nInserire una delle seguenti opzioni: \"iscrivi\", \"annulla\", \"visualizza\", \"elimina\", \"esci\": ")
#         if opzione == "iscrivi":
#             if corsi[nome_corso] > 0:
#                 corsi[nome_corso] -= 1
#                 print(f"\nComplimenti, ti sei iscritto al corso di {nome_corso}!")
#             else:
#                 print(f"\nMi dispiace, non ci sono posti disponibili al corso di {nome_corso}:/")
        
#         elif opzione == "annulla":
#             if corsi[nome_corso] < 100:
#                 corsi[nome_corso] += 1
#                 print(f"\nIscrizione annullata {nome_corso}!")
#             else:
#                 print(f"\nTutti i posti sono disponibili al corso di {nome_corso}:)")
        
#         elif opzione == "visualizza":
#             posti_liberi = corsi[nome_corso]
#             posti_occupati = 100 - corsi[nome_corso]
#             print(f"\nCi sono {posti_liberi} posti disponibili al corso di {nome_corso}.")
#             print(f"\nCi sono {posti_occupati} posti occupati al corso di {nome_corso}.")
            
#         elif opzione == "elimina":
#             messaggio = input(f"\nSei sicuro di voler eliminare il corso di {nome_corso}? Scegliere tra si o no: ").lower()
#             if messaggio == "si":
#                 corsi[nome_corso] = 100 # si ripristina il numero di posti occupati per il corso scelto
#                 print(f"\nIl corso {nome_corso} è stato eliminato. Tutte le iscrizioni sono state annullate.")
#                 break
#             else:
#                 print("\nEliminazione annullata")

#         elif opzione == "esci":
#             print("\nA presto!")
#             break

#         else:
#             print("\nOpzione non valida. Inserire una delle seguenti opzioni: \"iscrivi\", \"annulla\", \"visualizza\", \"elimina\", \"esci\".")



# Uso di match

corsi = {
    "matematica": 100,
    "informatica": 100,
    "inglese": 100,
}

while True:
    nome_corso = input("\nInserire il nome di un corso, tra informatica, matematica e inglese: ").lower()      

    if nome_corso not in corsi:
        print("\nCorso non valido. Scegliere uno dei corsi tra le opzioni.")
        continue

    while True:
        opzione = input("\nInserire una delle seguenti opzioni: \"iscrivi\", \"annulla\", \"visualizza\", \"elimina\", \"esci\": ")
        
        match opzione:
            case "iscrivi":
                if corsi[nome_corso] > 0:
                    corsi[nome_corso] -= 1
                    print(f"\nComplimenti, ti sei iscritto al corso di {nome_corso}!")
                else:
                    print(f"\nMi dispiace, non ci sono posti disponibili al corso di {nome_corso}:/")

            case "annulla":
                if corsi[nome_corso] < 100:
                    corsi[nome_corso] += 1
                    print(f"\nIscrizione annullata {nome_corso}!")
                else:
                    print(f"\nTutti i posti sono disponibili al corso di {nome_corso}:)")
        
            case "visualizza":
                posti_liberi = corsi[nome_corso]
                posti_occupati = 100 - corsi[nome_corso]
                print(f"\nCi sono {posti_liberi} posti disponibili al corso di {nome_corso}.")
                print(f"\nCi sono {posti_occupati} posti occupati al corso di {nome_corso}.")
            
            case "elimina":
                messaggio = input(f"\nSei sicuro di voler eliminare il corso di {nome_corso}? Scegliere tra si o no: ").lower()
                if messaggio == "si":
                    corsi[nome_corso] = 100 # si ripristina il numero di posti occupati per il corso scelto
                    print(f"\nIl corso {nome_corso} è stato eliminato. Tutte le iscrizioni sono state annullate.")
                    break
                else:
                    print("\nEliminazione annullata")

            case "esci":
                print("\nA presto!")
                break

            case _:
                print("\nOpzione non valida. Inserire una delle seguenti opzioni: \"iscrivi\", \"annulla\", \"visualizza\", \"elimina\", \"esci\".")



