cities = {
    "Parigi": {
        "Country": "Francia",
        "Continent": "Europa",
        "Population": "3 milioni",
        "Fact": "Conosciuta come la Città della Luce",
        "Celebrity": "Omar Sy"
    },
    "Roma": {
        "Country": "Italia",
        "Continent": "Europa",
        "Population": "4 milioni",
        "Fact": "Tutte le strade portano a Roma, Caput Mundi",
        "Celebrity": "Niccolò Paganini"
    },
    "Amsterdam": {
        "Country": "Paesi Bassi",
        "Continent": "Europa",
        "Population": "1 milione",
        "Fact": "Qui si fuma tranquillamente",
        "Celebrity": "Van Gogh"
    },
    "Dallas": {
        "Country": "Stati Uniti",
        "Continent": "America",
        "Population": "1.3 milioni",
        "Fact": "Terra di blues",
        "Celebrity": "Stevie Ray Vaughan"
    },
    "Tokyo": {
        "Country": "Giappone",
        "Continent": "Asia",
        "Population": "1.3 milioni",
        "Fact": "Qui si trovano un sacco di angurie quadrate",
        "Celebrity": "Katsushika Hokusai"
    }
}

for city, info in cities.items():
    print(f"Città: {city}")
    print(f"Paese: {info['Country']}")
    print(f"Continente: {info['Continent']}")
    print(f"Popolazione: {info['Population']}")
    print(f"Curiosità: {info['Fact']}")
    print(f"Celebrità: {info['Celebrity']}")
    print("-" * 60)