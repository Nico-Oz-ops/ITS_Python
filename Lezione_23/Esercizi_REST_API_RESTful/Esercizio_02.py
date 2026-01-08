'''
2. Metodi HTTP e CRUD: Per ciascuna operazione indica il metodo HTTP e il codice di stato corretto:

    Creare un nuovo corso
    Aggiornare i dati di un istruttore
    Eliminare un iscritto
    Ottenere l’elenco dei corsi
    Tentare di accedere a un corso inesistente
'''


'''
METODI HTTP E CRUD

    **Operazione**                **Metodo HTTP**         **URI tipico**           **Codice di stato RESTful**
- Creare un nuovo corso                POST           /courses                            201 Created
- Aggiornare i dati di             PUT (o PATCH)      /instructors/<instructor_id>        200 OK 
  un istruttore 
- Eliminare un iscritto               DELETE          /members/<member_id>                204 No Content
- Ottenere l'elenco dei corsi          GET            /courses                            200 OK
- Tentare di accedere a un corso       GET            /courses/<course_id>                404 Not Found
  inesistente
'''

from flask import Flask, jsonify, request

app = Flask(__name__)

# Creo dati fittizzi in memoria
courses = [
    {"id": 1, "name": "Yoga Base"},
    {"id": 2, "name": "Pilates Avanzato"}
]

instructors = [
    {"id": 1, "name": "Lilo Landa"},
    {"id": 2, "name": "Rosamel Fierro Delgado"}
]

members = [
    {"id": 1, "name": "Maurizio Rossi"},
    {"id": 2, "name": "Giovanni Verdi"}
]

# Creo le rotte per i corsi (courses)
@app.route("/courses", methods=["GET"])
def get_courses():
    return jsonify(courses), 200 # in questa maniera ottengo l'elenco dei corsi

# Tentare di accedere a un corso inesistente
@app.route("/courses/<int:course_id>", methods=["GET"])
def get_course(course_id):
    course = next((corso for corso in courses if corso["id"] == course_id), None)
    if course:
        return jsonify(course), 200
    
    else:
        return jsonify({"error": "Course not found"}), 404 # Corso inesistente

# Creo nuovo corso
@app.route("/courses", methods=["POST"])
def create_course():
    data = request.get_json()
    new_course = {"id": len(courses) + 1, "name": data["name"]}
    courses.append(new_course)
    return jsonify(new_course), 201 # Creare nuovo corso

# Creo le rotte per gli istruttori (instructors) e aggiornare i loro dati
@app.route("/instructors/<int:instructor_id>", methods=["PUT"])
def update_instructor(instructor_id):
    data = request.get_json() # prendo i dati dal corpo della richiesta, e li salvo in data. Serve per aggiornare i dati dell'istruttore
    instructor = next((inst for inst in instructors if inst["id"] == int(instructor_id)), None)

    if not instructor:
        return jsonify({"error": "Instructor not found"}), 404
    
    instructor["name"] = data.get("name", instructor["name"]) # aggiorno il nome dell'istruttore
    return jsonify(instructor), 200 # Aggiornare i dati di un istruttore

# - data è un dizionario che contiene i dati inviati nella richiesta HTTP, tipicamente
# ottenuti da una richiesta POST o PUT con un payload JSON, cioè
# da request.get_json().

# -.get(key, default) è un metodo dei dizionari in Python che restituisce il valore associato a key
# se esiste; altrimenti, restituisce default. In questo caso, se "name" non è presente in data,
# viene mantenuto il valore corrente instructor["name"].

# Creo le rotte per gli iscritti (members) e elimino un iscritto
@app.route("/members/<int:member_id>", methods=["DELETE"])
def delete_member(member_id):
    global members # uso global per modificare la variabile members definita all'esterno della funzione
    member = next((mem for mem in members if mem["id"] == int(member_id)), None) # cerco l'iscritto con l'id specificato
    if not member:
        return jsonify({"error": "Member not found"}), 404 # iscritto non trovato
    members = [mem for mem in members if mem["id"] != int(member_id)] # rimuovo l'iscritto dalla lista, creando una nuova lista senza di lui
    return '', 204 # Eliminare un iscritto, ritorno 204 No Content



