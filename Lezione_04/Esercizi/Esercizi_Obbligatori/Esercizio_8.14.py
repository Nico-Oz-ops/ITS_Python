# Esercizio 8.14 - Auto

# Uso di parametri arbitrari, dinamico (**kwargs)
def make_car(produttore, modello, **kwargs):
    car = {"produttore_auto": produttore, 
           "modello_auto": modello, 
           }
    
    for key, value in kwargs.items():
        car[key] = value

    return car

info_auto = make_car("subaru", "outback", colore="blu", pacchetto_traino=True, anno=2023)
info_auto_2 = make_car("porsche","911", colore="rosso", pacchetto_traino=False)

print(info_auto)
print("-" * 50)
print(info_auto_2)

# Opzione con una stampa più elegante
def make_car(produttore, modello, **kwargs):
    car = {"produttore_auto": produttore, 
           "modello_auto": modello, 
           }
    
    for key, value in kwargs.items():
        car[key] = value

    return car

info_auto = make_car("subaru", "outback", colore="blu", pacchetto_traino=True, anno=2023)
info_auto_2 = make_car("porsche","911", colore="rosso", pacchetto_traino=False)

print("Informazione Auto")
for key, value in info_auto.items():
    print(f"{key.capitalize()}: {value}")


# Uso di parametri fissi
def make_car(produttore, modello, colore, pacchetto_traino=True):
    car = {"produttore_auto": produttore, 
           "modello_auto": modello, 
           "colore_auto": colore, 
           "caratteristica_opzionale": pacchetto_traino}
    return car

info_auto = make_car("Subaru", "Outback", "Blu")
info_auto_2 = make_car("Porsche","911", "Rosso", False)


print(f"Produttore: {info_auto['produttore_auto']}.")
print(f"Modello: {info_auto['modello_auto']}.")
print(f"Colore: {info_auto['colore_auto']}.")
print(f"Pacchetto di Traino (caratteristiza opzionale): {info_auto['caratteristica_opzionale']}.")
print("-" * 50)

print(f"Produttore: {info_auto_2['produttore_auto']}.")
print(f"Modello: {info_auto_2['modello_auto']}.")
print(f"Colore: {info_auto_2['colore_auto']}.")
print(f"Pacchetto di Traino (caratteristiza opzionale): {info_auto_2['caratteristica_opzionale']}.")