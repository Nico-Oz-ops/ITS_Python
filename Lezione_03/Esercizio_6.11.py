cities = {
    "Parigi": {
        "country": "Francia",
        "population": "3 milioni",
        "fact": "Conosciuta come la Città della Luce"
    },
    "Roma": {
        "country": "Italia",
        "population": "4 milioni",
        "fact": "Tutte le strade portano a Roma, Caput Mundi"
    },
    "Amsterdam": {
        "country": "Paesi Bassi",
        "population": "1 milione",
        "fact": "Qui si fuma tranquillamente"
    }
}

for city, info in cities.items():
    print(f"Citta: {city}")
    print(f"Paese: {info['country']}")
    print(f"Popolazione: {info['population']}")
    print(f"Curiosità: {info['fact']}")
    print("-" * 50)