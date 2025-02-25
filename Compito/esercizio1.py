while True:
    parola = input("Inserire una serie di parole, se vuoi finire digitare 'fine': ")

    if parola.lower() == "fine":
        break
    if parola.lower()[0] == parola.lower()[-1]:
        print(f"Il primo e l'ultimo carattere della parola \"{parola}\" sono uguali.")
    else:
        print(f"Il primo e l'ultimo carattere della parola \"{parola}\" non sono uguali.")


