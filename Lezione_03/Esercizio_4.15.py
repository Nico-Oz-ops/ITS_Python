# Code Review

# 1 - Checking Usernames

# Definire la lista di usernames
current_users = [
    "kIKo", "sAKi", "jugo", 
    "maki", "niko",
]
# Creare una nuova lista di usernames
new_users = [
    "lizard", "mOKo", 
    "kiko", "saki", "telo",
]

# Imposta gli username della lista "current_users" in carattere minuscolo creandone una nuova
current_users_lower = [user.lower() for user in current_users]

# Controlla se ci sono usernames della lista "new_users" che si ripetono nella lista "current_users_lower"
for user in new_users:
    if user.lower() in current_users_lower:
        print(f"The username \"{user}\" is already exists. Please enter a new username.")
    else:
        print(f"Super! \"{user}\" is available.")

# 2 - Ordinal Numbers

# Lista "numbers" vuota
numbers = []

# Si aggiungono numeri alla lista vuota "numbers" e si controllano i numeri in un rango da 1 a 9
for number in range(1, 10):
    numbers.append(number)
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")

# 3 - Extensions

# Si definisce un dizionario "cities", con il nome di una città come chiave, e un dizionario (annidato)
# come valore con informazioni relative alla chiave (città)
cities = {
    "Parigi": {
        "country": "Francia",
        "continent": "Europa",
        "population": "3 milioni",
        "fact": "Conosciuta come la Città della Luce",
        "celebrity": "Omar Sy"
    },
    "Roma": {
        "country": "Italia",
        "continent": "Europa",
        "population": "4 milioni",
        "fact": "Tutte le strade portano a Roma, Caput Mundi",
        "celebrity": "Niccolò Paganini"
    },
    "Amsterdam": {
        "country": "Paesi Bassi",
        "continent": "Europa",
        "population": "1 milione",
        "fact": "Qui si fuma tranquillamente",
        "celebrity": "Van Gogh"
    },
    "Dallas": {
        "country": "Stati Uniti",
        "continent": "America",
        "population": "1.3 milioni",
        "fact": "Terra di blues",
        "celebrity": "Stevie Ray Vaughan"
    },
    "Tokyo": {
        "country": "Giappone",
        "continent": "Asia",
        "population": "1.3 milioni",
        "fact": "Qui si trovano un sacco di angurie quadrate",
        "celebrity": "Katsushika Hokusai"
    }
}

# Itera su ogni coppia chiave-valore nel dizionario "cities"
for city, info in cities.items():
    print(f"Città: {city}")
    print(f"Paese: {info['country']}")
    print(f"Continente: {info['continent']}")
    print(f"Popolazione: {info['population']}")
    print(f"Curiosità: {info['fact']}")
    print(f"Celebrità: {info['celebrity']}")
    print("-" * 60)