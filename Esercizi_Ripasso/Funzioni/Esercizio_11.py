# Esercizio 11
'''Nomi delle città: scrivi una funzione chiamata city_country() che prenda il nome di una città e del suo paese. 
La funzione dovrebbe restituire una stringa formattata in questo modo: "Santiago, Cile". 
Chiama la tua funzione con almeno tre coppie città-paese e stampa i valori restituiti.'''

def city_country(city:str, country:str):
    print(f"{city}, {country}.")

city_country("Santiago", "Cile")
city_country("Londra", "Inghilterra")
city_country("Dakar", "Senegal")


def city_country(city, country):
    return f"{city}, {country}."

print(city_country("Santiago", "Cile"))
print(city_country("Londra", "Inghilterra"))
print(city_country("Dakar", "Senegal"))
