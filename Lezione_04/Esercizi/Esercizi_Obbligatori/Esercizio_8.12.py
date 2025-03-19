# Esercizio 8.12 - Sandwich

def sandwich_ordinato(*args):

    riepilogo = []
    for item in args:
        riepilogo.append(item)

    print(f"Il sandwich ordinato contiene: {riepilogo}")

sandwich_ordinato("hamburguer", "formaggio", "rucola")
sandwich_ordinato("hamburguer", "formaggio", "pomodoro")
sandwich_ordinato("tofu", "funghi", "lattuga")
print("-" * 50)


# Con l'uso del metodo .join(), che serve a unire gli elementi di una sequenza in una stringa, 
# con la possibilità di specificare un separatore personalizzato

def sandwich_ordinato(*args):

    riepilogo = []
    for item in args:
        riepilogo.append(item)

    print(f"Il sandwich ordinato contiene: {', '.join(riepilogo)}")

sandwich_ordinato("hamburguer", "formaggio", "rucola")
sandwich_ordinato("hamburguer", "formaggio", "pomodoro")
sandwich_ordinato("tofu", "funghi", "lattuga")
print("-" * 50)

# E se volessi aggiungere le virgolette agli elementi stampati senza parentesi quadre...

def sandwich_ordinato(*args):

    riepilogo = []
    for item in args:
        riepilogo.append(item)
        riepilogo_con_virgolette = ['"{}"'.format(item) for item in riepilogo]

    print(f"Il sandwich ordinato contiene: {', '.join(riepilogo_con_virgolette)}")

sandwich_ordinato("hamburguer", "formaggio", "rucola")
sandwich_ordinato("hamburguer", "formaggio", "pomodoro")
sandwich_ordinato("tofu", "funghi", "lattuga")
