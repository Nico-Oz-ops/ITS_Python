cities = {
    "Parigi": {
        "Country": "Francia",
        "Population": "3 milioni",
        "Fact": "Conosciuta come la Città della Luce"
    },
    "Roma": {
        "Country": "Italia",
        "Population": "4 milioni",
        "Fact": "Tutte le strade portano a Roma, Caput Mundi"
    },
    "Amsterdam": {
        "Country": "Paesi Bassi",
        "Population": "1 milione",
        "Fact": "Qui si fuma tranquillamente"
    }
}

for city, info in cities.items():
    print(f"Citta: {city}")
    print(f"Paese: {info['Country']}")
    print(f"Popolazione: {info['Population']}")
    print(f"Curiosità: {info['Fact']}")
    print("-" * 50)