'''
Descrizione del Sistema
 
Il sistema gestisce una palestra digitale che offre allenamenti e consente ai membri di iscriversi, 
segnare i progressi sugli esercizi e visualizzare i loro allenamenti e progressi. Gli allenamenti 
sono composti da vari esercizi, ciascuno con un livello di difficoltà.
 
Classi Principali:
 
* Esercizio
* Allenamento
* Membro
* PalestraDigitale

A.  Classe: Esercizio
 
Ogni esercizio ha un nome, un livello di difficoltà e uno stato di completamento (completato/non completato).
 
Attributi:
 
* name: Il nome dell'esercizio (es. "Push-up").
* difficulty: La difficoltà dell'esercizio ("facile", "medio", "difficile").
* completed: Un booleano che indica se l'esercizio è stato completato dal membro.
 
Metodi:
* __init__(self, name: str, difficulty: str) -> None: Costruttore per creare un esercizio 
con un nome e una difficoltà.
 
* mark_completed(self) -> None: Imposta completed su True quando l'esercizio è completato.
 
* __str__(self) -> str: Restituisce una rappresentazione in formato stringa dell'esercizio 
(es. "Push-up (facile)").
 

B.  Classe: Allenamento
 
Ogni allenamento ha un nome e una lista di esercizi associati.
 
Attributi:
 
* workout_id: L'ID univoco dell'allenamento (es. "w01").
* workout_name: Il nome dell'allenamento (es. "Allenamento Cardio").
 
esercizi: Una lista di oggetti Esercizio associati a questo allenamento.
 
Metodi:
 
* __init__(self, workout_id: str, workout_name: str) -> None: Costruttore per creare un allenamento 
con un ID e un nome.
* add_exercise(self, exercise: Esercizio) -> None: Aggiunge un esercizio alla lista esercizi dell'allenamento.
* list_exercises(self) -> None: Stampa tutti gli esercizi associati all'allenamento.
 
C.   Classe: Membro
 
Ogni membro ha un ID, un nome e una lista di allenamenti a cui è iscritto. Inoltre, 
può segnare i progressi sugli esercizi.
 
Attributi:
 
* member_id: L'ID univoco del membro (es. "m01").
* name: Il nome del membro.
* allenamenti_iscritti: Una lista di oggetti Allenamento a cui il membro è iscritto.
 
Metodi:
 
* __init__(self, member_id: str, name: str) -> None: Costruttore per creare un membro con un ID e un nome.

* enroll_in_workout(self, workout: Allenamento) -> None: Iscrive il membro a un allenamento, 
se non è già iscritto.

* mark_exercise_completed(self, workout: Allenamento, exercise_name: str) -> None: Segna come completato 
un esercizio specifico all'interno di un allenamento.

* __str__(self) -> str: Restituisce una rappresentazione in formato stringa del membro, con il suo nome e ID.
 

D.  Classe: PalestraDigitale
 
Gestisce l'aggiunta di allenamenti, l'iscrizione dei membri e la registrazione dei progressi.
 
Attributi:
 
* allenamenti: Un dizionario che mappa l'ID dell'allenamento (workout_id) all'oggetto Allenamento.
* membri: Un dizionario che mappa l'ID del membro (member_id) all'oggetto Membro.
 
Metodi:
 
* __init__(self) -> None: Costruttore per inizializzare la palestra digitale.
 
* add_workout(self, workout_id: str, workout_name: str) -> None: Aggiunge un allenamento alla palestra.
 
* add_exercise_to_workout(self, workout_id: str, exercise_name: str, difficulty: str) -> None: Aggiunge un 
  esercizio a un allenamento specificato.
 
* register_member(self, member_id: str, name: str) -> None: Registra un nuovo membro nella palestra.
 
* enroll_member_in_workout(self, member_id: str, workout_id: str) -> None: Iscrive un membro a un allenamento.
 
* list_member_workouts(self, member_id: str) -> None: Mostra tutti gli allenamenti a cui un membro è iscritto.
 
* list_member_exercises(self, member_id: str, workout_id: str) -> None: Mostra tutti gli esercizi di un 
  allenamento a cui un membro è iscritto, con il loro stato (completato/non completato).
 
* list_completed_exercises(self, member_id: str) -> None: Mostra tutti gli esercizi completati da un membro 
  in tutti gli allenamenti.
'''
class Esercizio:
    def __init__(self, name: str, difficulty: str) -> None:
        self.name = name
        self.difficulty = difficulty
        self.completed: bool = False

    def mark_completed(self) -> None:
        self.completed = True
    
    def __str__(self) -> str:
        return f"{self.name} ({self.difficulty})"

class Allenamento:
    def __init__(self, workout_id: str, workout_name: str) -> None:
        self.workout_id = workout_id
        self.workout_name = workout_name
        self.esercizi: list[Esercizio] = []

    def add_exercise(self, exercise: Esercizio) -> None:
        if not isinstance(exercise, Esercizio):
            raise ValueError("Esercizio non valido")
        
        if exercise not in self.esercizi:
            self.esercizi.append(exercise)
    
    def list_exercises(self) -> None:
        if not self.esercizi:
            print("La lista è vuota")
        
        print(", ".join([str(esercizio) for esercizio in self.esercizi]))
        # for esercizio in self.esercizi:
        #     print(esercizio.nome)

class Membro:
    def __init__(self, member_id: str, name: str) -> None:
        self.member_id = member_id
        self.name = name
        self.allenamenti_iscritti: list[Allenamento] = []
    
    def enroll_in_workout(self, workout: Allenamento) -> None:
        if workout not in self.allenamenti_iscritti:
            self.allenamenti_iscritti.append(workout)
    
    def mark_exercise_completed(self, workout: Allenamento, exercise_name: str) -> None:
        if workout not in self.allenamenti_iscritti:
            print(f"{self.name} non si trova nella lista di allenamenti iscritti")
            return
        
        for esercizio in workout.esercizi:
            if esercizio.name == exercise_name:
                esercizio.mark_completed()
                print(f"Esercizio '{exercise_name}' completato!")
                return
            
        print(f"Esercizio '{exercise_name}' non trovato in {workout.workout_name}")
    
    def __str__(self):
        return f"Membro: {self.name} - ID: {self.member_id}"

class PalestraDigitale:
    def __init__(self) -> None:
        self.allenamenti: dict[str, Allenamento] = {}
        self.membri: dict[str, Membro] = {}
    
    def add_workout(self, workout_id: str, workout_name: str) -> None:
        if workout_id not in self.allenamenti:
            self.allenamenti[workout_id] = Allenamento(workout_id, workout_name)
        else:
            print(f"L'allenamento '{workout_name}' con ID {workout_id} esiste già")
    
    def add_exercise_to_workout(self, workout_id: str, exercise_name: str, difficulty: str) -> None:
        if workout_id not in self.allenamenti: # controllo che workout si trovi nel dizionario di allenamenti
            raise ValueError("Id di workout non valido")
        
        workout = self.allenamenti[workout_id] #recupero l'oggetto Allenamento
        esercizio = Esercizio(exercise_name, difficulty) # creo un nuovo esercizio

        workout.add_exercise(esercizio) #aggiungo l'esercizio al workout 
    
    def register_member(self, member_id: str, name: str) -> None:
        if member_id not in self.membri:
            self.membri[member_id] = Membro(member_id, name)
        else:
            print(f"Il membro {name} con ID {member_id} esiste già")
    
    def enroll_member_in_workout(self, member_id: str, workout_id: str) -> None:
        if member_id not in self.membri:
            raise ValueError("Membro non registrato")
        
        if workout_id not in self.allenamenti:
            raise ValueError
        
        membro = self.membri[member_id] #recupero l'oggetto Membro
        workout = self.allenamenti[workout_id] #recupero l'oggetto Allenamento
        membro.enroll_in_workout(workout) #iscrivere un membro a un allenamento (workout)
    
    def list_member_workouts(self, member_id: str) -> None:
        if member_id not in self.membri:
            raise ValueError(f"Il membro con ID {member_id} non esiste")
        
        membro = self.membri[member_id]

        if not membro.allenamenti_iscritti:
            print(f"Il membro {member_id} non è iscritto ad alcun allenamento")
            return
        
        print(f"\nAllenamenti di {membro.name}:")
        for allenamento in membro.allenamenti_iscritti:
            print(f"{allenamento.workout_name} - ID: {allenamento.workout_id}")
    
    def list_member_exercises(self, member_id: str, workout_id: str) -> None:
        if member_id not in self.membri:
            raise ValueError("Membro non registrato")
        
        if workout_id not in self.allenamenti:
            raise ValueError("L'allenamento non esiste")
        
        membro = self.membri[member_id]
        workout = self.allenamenti[workout_id]

        if workout not in membro.allenamenti_iscritti:
            print(f"'{membro.name}' non è iscritto all'allenamento '{workout.workout_name}'")
            return
        
        print(f"\nGli esercizi di '{membro.name}' per l'allenamento '{workout.workout_name}':")
        if not workout.esercizi:
            print(f"Nessun esercizio disponibile")
            return
        
        for esercizio in workout.esercizi:
            stato = "Completato" if esercizio.completed else "Non completato"
            print(f"{esercizio.name} {esercizio.difficulty} - {stato}")
            
    
    def list_completed_exercises(self, member_id: str) -> None:
        if not member_id in self.membri:
            raise ValueError(f"Membro '{member_id}' non esiste")
        
        membro = self.membri[member_id]
        esercizi_completati = []

        for allenamento in membro.allenamenti_iscritti:
            for esercizio in allenamento.esercizi:
                if esercizio.completed:
                    esercizi_completati.append((allenamento.workout_name, esercizio.name))
        
        if not esercizi_completati:
            print("Ancora non è stato completato nessun esercizio")
            return
        
        print(f"\nEsercizi completati da {membro.name}:")
        for workout_name, esercizio_name in esercizi_completati:
            print(f"- {esercizio_name} da {workout_name}")

if __name__=="__main__":

    # Creazione palestra e dati
    palestra = PalestraDigitale()
    palestra.add_workout("w01", "Allenamento Cardio")
    palestra.add_exercise_to_workout("w01", "Corsa", "medio")
    palestra.add_exercise_to_workout("w01", "Squat", "medio")

    palestra.register_member("m01", "Nicolás")
    palestra.enroll_member_in_workout("m01", "w01")

    # Completamento di un esercizio
    membro = palestra.membri["m01"]
    allenamento = palestra.allenamenti["w01"]
    membro.mark_exercise_completed(allenamento, "Corsa")

    # Visualizzazioni
    palestra.list_member_workouts("m01")
    palestra.list_member_exercises("m01", "w01")
    palestra.list_completed_exercises("m01")

        # Creo un allenamento
    cardio = Allenamento("w01", "Allenamento Cardio")

    # Aggiungo due esercizi
    cardio.add_exercise(Esercizio("Corsa", "medio"))
    cardio.add_exercise(Esercizio("Squat", "facile"))

    # ✅ Chiamata al metodo da testare
    cardio.list_exercises()

