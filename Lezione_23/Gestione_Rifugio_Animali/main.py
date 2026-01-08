'''
In questo esercizio dovrai scrivere il codice per un sistema che gestisce gli animali di un rifugio 
e che espone alcune informazioni e funzionalità tramite un’applicazione Flask. 
L’obiettivo è applicare i principi di ereditarietà e classi astratte, e sperimentare sia le richieste 
HTTP GET sia le richieste HTTP POST.

Specifiche del Problema

**Classe Animal**
La classe Animal rappresenta un animale generico del rifugio. È una classe astratta e non può essere istanziata direttamente.

Ogni animale ha:

    * un identificativo id di tipo stringa (es. "d1", "c3"),
    * un nome name di tipo stringa,
    * un’età age_years di tipo intero (anni),
    * un peso weight_kg di tipo float (chilogrammi).

Metodi:

    * species(): metodo astratto.
    Deve essere implementato nelle sottoclassi per restituire la specie dell’animale, ad esempio "dog" o "cat".

    * daily_food_grams(): metodo astratto.
    Deve essere implementato nelle sottoclassi e deve restituire la quantità di cibo giornaliera raccomandata in grammi.

    * info(): metodo concreto.
    Restituisce un dizionario con le informazioni principali dell’animale, ad esempio:
    { "id": ..., "name": ..., "species": ..., "age_years": ..., "weight_kg": ..., # più eventuali campi specifici delle sottoclassi }

    * bmi_like(): metodo concreto che restituisce un valore derivato (simile a un indice di “forma fisica”), ad esempio calcolato come:
    weight_kg / (age_years + 1)

    Il dettaglio della formula è lasciato libero, l’importante è che sia coerente e restituisca un numero (float).

**Classe Dog**
La classe Dog rappresenta un cane e eredita da Animal.

Attributi aggiuntivi:

    * breed: razza del cane, stringa (es. "labrador"),
    * is_trained: booleano che indica se il cane è addestrato (True/False).

Metodi:

    * species(): restituisce la stringa "dog".

    * daily_food_grams(): restituisce la quantità di cibo giornaliero in grammi.
    Puoi usare una formula plausibile, ad esempio:
    return 200 + age_years * 50

    oppure un’altra a tua scelta, purché sia chiaro che il risultato rappresenta grammi di cibo al giorno.

    * info(): estende il metodo della superclasse includendo anche breed e is_trained.

**Classe Cat**

La classe Cat rappresenta un gatto e eredita da Animal.

Attributi aggiuntivi:

    * indoor_only: booleano che indica se il gatto vive solo in casa (True/False),
    * favorite_toy: stringa che rappresenta il gioco preferito (es. "ball", "mouse").

Metodi: 

    * species(): restituisce la stringa "cat".

    * daily_food_grams(): restituisce la quantità di cibo giornaliero in grammi.
    Anche qui puoi usare una formula plausibile, ad esempio:
    return 100 + age_years * 30

    * info(): estende il metodo della superclasse includendo anche indoor_only e favorite_toy.

**Classe Shelter**

La classe Shelter rappresenta il contenitore principale del sistema, che gestisce tutti gli animali presenti nel rifugio.

Attributi:

    * animals: dizionario che associa a ogni identificativo (id) l’oggetto Animal corrispondente, ad esempio:
    { "d1": <Dog ...>, "c1": <Cat ...>, ... }

    * adoptions (opzionale ma consigliato): struttura dati per gestire lo stato di adozione, ad esempio un dizionario:
    { "d1": "Mario Rossi", "c1": "Luca Bianchi" }

    * dove la chiave è l’id dell’animale e il valore è il nome dell’adottante.

Metodi:

    * add(animal): aggiunge un animale al rifugio.
    Se esiste già un animale con lo stesso id, puoi decidere se sovrascriverlo o ignorare l’operazione 
    (nel contesto dell’esercizio è sufficiente una scelta semplice e documentata nei commenti).

    * get(animal_id): restituisce l’oggetto Animal corrispondente all’ID specificato oppure None se non esiste.

    * list_all(): restituisce una lista di tutte le istanze di Animal presenti nel rifugio (puoi decidere se 
    restituire direttamente gli oggetti o piuttosto una lista di dizionari generati con info()).

    * is_adopted(animal_id): restituisce True/False a seconda che l’animale risulti adottato nella struttura adoptions.

    * set_adopted(animal_id, adopter_name): registra l’adozione per un dato animale, salvando il nome dell’adottante.

Nel codice principale dovrà essere creato un rifugio e dovranno essere creati almeno due animali, uno di tipo Dog 
e uno di tipo Cat, che saranno aggiunti al rifugio prima di avviare l’app Flask.
'''
#------------------------------------------------------FLASK------------------------------------------------------------------#
'''
Applicazione Flask

Crea un’applicazione Flask che esponga alcune route GET per consultare i dati del rifugio e alcune route POST per 
modificare lo stato (ad esempio aggiungere animali e registrare adozioni).
Le funzioni delle route devono restituire oggetti JSON (non stringhe semplici).

Route GET richieste:

* 1. GET /

Restituisce un JSON con:

    una breve descrizione del servizio, ad esempio:
     
    { "message": "Welcome to Animal Shelter API" }

    alcuni link testuali che indicano le altre route disponibili, ad esempio:

        /animals

        /animals/d1

        /animals/d1/food

        /animals/d1/adoption

    Questi link devono essere generati dinamicamente con url_for() e poi inseriti nel JSON, ad esempio:
    { "message": "...", "links": { "list_animals": url_for("list_animals"), "sample_dog": url_for("get_animal", animal_id="d1"), ... } }

* 2. GET /animals

Restituisce un JSON con la lista degli animali presenti nel rifugio.

Ogni elemento della lista può essere:

    una stringa descrittiva, ad esempio
    "d1 - Rex (dog) - 2 years - 18.5kg",

    oppure

    un dizionario con i campi principali dell’animale (quelli restituiti da info()).

La scelta è libera, ma deve essere coerente in tutto il programma (se scegli la rappresentazione come dizionario, 
usala ovunque per le liste).

* 3. GET /animals/<animal_id>

Restituisce un JSON con un solo elemento che rappresenta i dettagli dell’animale con l’ID specificato.

Ad esempio:
{ "id": "d1", "name": "Rex", "species": "dog", "age_years": 2, "weight_kg": 18.5, "breed": "border collie", "is_trained": true }

Se l’animale non esiste, la route dovrebbe restituire un JSON di errore (es. {"error": "Animal not found"}) con 
status code appropriato (ad esempio 404).

* 4. GET /animals/<animal_id>/food

Restituisce un JSON con le informazioni sul cibo giornaliero stimato per l’animale specificato.

L’output può essere, ad esempio:
{ "id": "d1", "daily_food_grams": 350 }

oppure una struttura più ricca a tua scelta, purché sia JSON.

Anche qui, se l’animale non esiste, va gestito l’errore.

* 5. GET /animals/<animal_id>/adoption

Restituisce lo stato di adozione dell’animale specificato.

Esempi di output:

Animale non adottato:
{ "id": "d1", "adopted": false }

Animale adottato:
{ "id": "d1", "adopted": true, "adopter_name": "Mario Rossi" }
'''

'''
1. POST /animals/add

Permette di aggiungere un nuovo animale al rifugio.

Il body JSON deve contenere le informazioni necessarie per creare l’animale e un campo che 
specifica il tipo, ad esempio "dog" o "cat".

Esempio per un cane:
{ "type": "dog", "id": "d3", "name": "Rex", "age_years": 2, "weight_kg": 18.5, "breed": "border collie", "is_trained": true }

Esempio per un gatto:
{ "type": "cat", "id": "c5", "name": "Micia", "age_years": 3, "weight_kg": 4.2, "indoor_only": true, "favorite_toy": "ball" }

La funzione della route deve:

    - leggere il JSON dalla richiesta;

    - verificare che il campo "type" sia presente e valido ("dog" o "cat");

    - controllare che i campi richiesti (id, name, ecc.) siano presenti;

    - creare l’istanza della sottoclasse corretta (Dog o Cat);

    - aggiungere l’animale al Shelter con shelter.add(...);

    - restituire un JSON di conferma, ad esempio:
    { "status": "ok", "added": { "id": "d3", "species": "dog" } }

In caso di errore (id già esistente, campi mancanti, tipo non riconosciuto) 
deve restituire un JSON di errore con uno status code adeguato (es. 400 Bad Request).
'''


'''
2. POST /animals/<animal_id>/adopt

Registra l’adozione di un animale.

Il body JSON deve contenere almeno il nome dell’adottante, ad esempio:
{ "adopter_name": "Mario Rossi" }

La funzione della route deve:

    verificare che l’animale con id animal_id esista nel rifugio;

    leggere il nome dell’adottante dal JSON;

    aggiornare la struttura di adozioni del Shelter (ad esempio con shelter.set_adopted(animal_id, adopter_name));

    restituire un JSON di conferma, ad esempio:
    { "id": "d1", "adopted": true, "adopter_name": "Mario Rossi" }

Se l’animale non esiste, oppure è già adottato (se vuoi gestire anche questo caso), la route deve restituire 
un JSON di errore e uno status code appropriato (es. 404 o 400).
'''

from flask import Flask, jsonify, request, url_for
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, id: str, name: str, age_years: int, weight_kg: float):
        self.id = id
        self.name = name
        self.age_years = age_years
        self.weight_kg = weight_kg
    
    @abstractmethod
    def species(self) -> str:
        pass

    @abstractmethod
    def daily_food_grams(self) -> float:
        pass

    def info(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "species": self.species(),
            "age_years": self.age_years,
            "weight_kg": self.weight_kg
            }
    
    def bmi_like(self) -> float:
        return self.weight_kg / (self.age_years + 1)
    
class Dog(Animal):
    def __init__(self, id: str, name: str, age_years: int, weight_kg: float, breed: str, is_trained: bool):
        super().__init__(id, name, age_years, weight_kg)
        self.breed = breed
        self.is_trained = is_trained
    
    def species(self) -> str:
        return "dog"
    
    def daily_food_grams(self) -> float:
        return 200 + self.age_years * 50
    
    def info(self) -> dict:
        info_base = super().info()
        info_base.update({
            "breed": self.breed,
            "is_trained": self.is_trained
        })
        return info_base

class Cat(Animal):
    def __init__(self, id: str, name: str, age_years: int, weight_kg: float, indoor_only: bool, favorite_toy: str):
        super().__init__(id, name, age_years, weight_kg)
        self.indoor_only = indoor_only
        self.favorite_toy = favorite_toy
    
    def species(self) -> str:
        return "cat"

    def daily_food_grams(self) -> float:
        return 100 + self.age_years * 30
    
    def info(self) -> dict:
        info_base = super().info()
        info_base.update({
            "indoor_only": self.indoor_only,
            "favorite_toy": self.favorite_toy
            })
        return info_base

class Shelter:
    def __init__(self):
        self.animals: dict[str, Animal] = {}
        self.adoptions: dict[str, str] = {}

    def add(self, animal: Animal) -> None:
        self.animals[animal.id] = animal # aggiungo un animale al rifugio, sovrascrivendo se l'id esiste già

    # Se volessi maggiore controllo sull'aggiunta ed evitare sovrascritture (perdita di dati), potrei fare così:
        # if animal.id in self.animals:
        #     # Se l'animale con lo stesso id esiste già, lo sovrascrivo
        #     raise ValueError(f"L'animale con l'id {animal.id} esiste già nel rifugio.")
        # self.animals[animal.id] = animal
    
    def get(self, animal_id: str) -> Animal|None:
        return  self.animals.get(animal_id, None) # restituisco l'animale corrispondente all'id o None se non esiste
    # l'uso di dict.get() è più conciso e leggibile. Cerca l'animale_id (key nel dizionario) e restituisce None se non trovato.

    # alternativa:
        # if animal_id in self.animals:
        #     return self.animals[animal_id]
        # return None
    
    def list_all(self) -> list[Animal]:
        return list(self.animals.values()) # restituisco una lista di tutte le istanze di Animal presenti nel rifugio
    # uso dict.values() per ottenere direttamente gli oggetti Animal, più efficiente e leggibile.

    def is_adopted(self, animal_id: str) -> bool:
        return animal_id in self.adoptions # restituisco True/False se l'animale è adottato
    
    def set_adopted(self, animal_id: str, adopter_name: str) -> None:
        self.adoptions[animal_id] = adopter_name # registro l'adozione salvando il nome dell'adottante

if __name__ == "__main__":
    
    shelter = Shelter()

    dog1 = Dog(id="1", name="Jack", age_years=10, weight_kg=30.5, breed="pastore tedesco", is_trained=True)
    cat1 = Cat(id="2", name="Sunday", age_years=12, weight_kg=5.2, indoor_only=True, favorite_toy="mouse")

    shelter.add(dog1)
    shelter.add(cat1)

    app = Flask(__name__)

    #---------------------------------
    # 1. ROOT /
    #---------------------------------
    @app.route("/", methods=["GET"])
    def index():
        links = {"list_animals": url_for("list_animals")} # creo un dizionario di link dinamici url_for(). Questo è il link princiaple

        # aggiunta dinamica del resto dei link per tutti gli animali presenti nel rifugio
        for animal in shelter.list_all():
            links[f"{animal.species()}_{animal.id}"] = url_for("get_animal", animal_id=animal.id)
            links[f"{animal.species()}_{animal.id}_food"] = url_for("get_animal_food", animal_id=animal.id)
            links[f"{animal.species()}_{animal.id}_adoption"] = url_for("get_animal_adoption", animal_id=animal.id)
        
        return jsonify({
            "message": "Welcome to Animal Shelter API",
            "links": links
        }), 200

    #---------------------------------
    # 2. GET /animals
    #---------------------------------
    @app.route("/animals", methods=["GET"])
    def list_animals():
        # restituire una lista di dizionari con tutte le info degli animali
        animals_info = [animal.info() for animal in shelter.list_all()]
        return jsonify({"animals": animals_info}), 200 # leggere la lista degli animali presenti nel rifugio
    
    #---------------------------------
    # 3. GET /animals/<animal_id>
    #---------------------------------
    @app.route("/animals/<string:animal_id>", methods=["GET"])
    def get_animal(animal_id: str):
        animal = shelter.get(animal_id)
        if animal is None:
            return jsonify({"error": "Animal not found"}), 404 # animale non esistente
    
        return jsonify(animal.info()), 200 # leggere i dettagli di un singolo animale

    #---------------------------------
    # 4. GET /animals/<animal_id>/food
    #---------------------------------
    @app.route("/animals/<string:animal_id>/food", methods=["GET"])
    def get_animal_food(animal_id: str):
        animal = shelter.get(animal_id)
        if animal is None:
            return jsonify({"error": "Animal not found"}), 404
        
        return jsonify({
            "animal_id": animal.id, 
            "daily_food_grams": animal.daily_food_grams()
            }), 200 # leggere le informazioni sul cibo giornaliero stimato per un animale specifico

    #---------------------------------
    # 5. GET /animals/<animal_id>/adoption
    #---------------------------------
    @app.route("/animals/<string:animal_id>/adoption", methods=["GET"])
    def get_animal_adoption(animal_id: str):
        animal = shelter.get(animal_id)
        if animal is None:
            return jsonify({"error": "Animal not found"}), 404
        
        adopted = shelter.is_adopted(animal_id)
        if adopted:
            adopter_name = shelter.adoptions[animal_id]
            return jsonify({
                "animal_id": animal.id, # è l’attributo dell’oggetto che rappresenta l'id dell’animale
                "adopted": True, 
                "adopter_name": adopter_name
                }), 200 # leggere lo stato di adozione di un animale specifico (adottato)
        else:
            return jsonify({
                "animal_id":animal.id, 
                "adopted": False
                }), 200 # leggere lo stato di adozione di un animale specifico (non adottato)
    
    #---------------------------------
    # 1. POST /animals/add
    #---------------------------------
    @app.route("/animals/add", methods=["POST"])
    def add_animal():
        # leggo il body JSON
        data = request.get_json()
        if not data:
            return jsonify({"error": "Missing JSON body"}), 400
        

        # verifico il campo "type"
        animal_type = data.get("type") # prende il valore associato alla chiave "type", se nel JSON non esiste "type" restituisce None
        if animal_type not in ("dog", "cat"):
            return jsonify({"error": "Invalid or missing animal type"}), 400
        
        # campi richiesti comuni presenti
        required_common = {"id", "name", "age_years", "weight_kg"}
        if not required_common.issubset(data.keys()): #issubset(...) è un metodo dei set che serve a verificare se tutti gli elementi di un insieme sono contenuti in un altro insieme
            # quindi, verifica se tutte le chiavi richieste siano presenti nel JSON, se anche una sola manca, errore
            return jsonify({"error":"Missing required fields"}), 400
        
        animal_id = data["id"] # estrae l'id dell'animale. Qui si usa [] perché sono sicuro che "id" esiste (ontrollato prima)
        
        # controllo che l'id dell'animale non esista
        if shelter.get(animal_id) is not None:
            return jsonify({"errore": "Animal with this id already exists"}), 400
        
        # creazione dell'animale corretto
        if animal_type == "dog":
            required_dog = {"breed", "is_trained"} # campi specifici del cane
            if not required_dog.issubset(data.keys()): # verifico che il JSON contenga tutto ciò che serve per un Dog
                return jsonify({"errore": "Missing dog specific fields"}), 400
            
            # ora si crea un oggetto di dominio (non dizionario, non JSON), Dog
            animal = Dog(
                id = data["id"],
                name = data["name"],
                age_years = data["age_years"],
                weight_kg = data["weight_kg"],
                breed = data["breed"],
                is_trained = data["is_trained"]
            )
        
        elif animal_type == "cat":
            required_cat = {"indoor_only", "favorite_toy"} # campi specifici del gatto
            # se almeno una delle chiavi richieste per il gatto non è presente nel JSON ricevuto (data.keys())
            # allora la validazione fallisce e viene restituito un errore 400
            if not required_cat.issubset(data.keys()):
                return jsonify({"errore": "Missing cat specific fields"}), 400
            
            # si crea l'oggetto di dominio, Cat
            animal = Cat(
                id = data["id"],
                name = data["name"],
                age_years = data["age_years"],
                weight_kg = data["weight_kg"],
                indoor_only = data["indoor_only"],
                favorite_toy = data["favorite_toy"]
            )
        
        # aggiungo l'animale al rifugio
        shelter.add(animal) # l'animale entra nel sistema e tutte le altre route ora lo "vedono"

        # risposta di conferma
        return jsonify({
            "status": "ok",
            "added": {
                "id": animal.id,
                "species": animal.species()
            }
        }), 201 # 201 Created 



    #---------------------------------
    # 2. POST /animals/<animal_id>/adopt
    #---------------------------------
    @app.route("/animals/<string:animal_id>/adopt", methods=["POST"])
    def adopt_animal(animal_id: str):
        # 1. verificio che l'animale esista
        animal = shelter.get(animal_id)
        if animal is None:
            return jsonify({"error": "Animal not found"}), 404 # animale non esistente
        
        # 2. verifico che l'animale non sia già adottato
        if shelter.is_adopted(animal_id):
            return jsonify({"error": "Animal already adopted"}), 400 # animale già adottato
        
        # 3. leggo il nome dell'adottante dal JSON
        data = request.get_json() # prendo i dati dal corpo della richiesta {"adopter_name": "Mario Rossi"}
        if not data or "adopter_name" not in data: # controllo che il campo adopter_name sia presente
            return jsonify({"error": "Adopter name is required"}), 400
        
        adopter_name = data["adopter_name"]

        # 4. registro l'adozione
        shelter.set_adopted(animal_id, adopter_name) # registro l'adozione nell'oggetto shelter

        # 5. restituisco un JSON di conferma
        return jsonify({                           # conferma in JSON dell'adozione 
            "animal_id": animal.id,
            "adopted": True,
            "adopter_name": adopter_name
        }), 200



    

    


