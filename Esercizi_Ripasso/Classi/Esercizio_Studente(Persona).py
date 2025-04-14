from Esercizio_Persona import Persona

class Studente(Persona):

    def __init__(self, nome, cognome, eta, corso_di_studi, voto_medio):

        if eta < 17:
            raise ValueError("Solitamente un studente universitario deve avere almeno 17 anni")
        
        super().__init__(nome, cognome, eta)
        self.corso_di_studi = corso_di_studi.title() # capitalizazzione del corso di studio
        self.voto_medio = voto_medio
    
    def __str__(self):
        return super().__str__() + f"\nCorso di studi: {self.corso_di_studi}\nVoto medio: {self.voto_medio}"
    
    def __call__(self):
        print(super().__call__()) # opzionale se si vuole stampare l'info dell call di Persona

        if self.voto_medio < 18:
            print(f"{self.getNome()} {self.getCognome()} ha bisogno di migliorare i suoi voti")
        
        else:
            print(f"{self.getNome()} {self.getCognome()} sta andando bene")

if __name__ == "__main__":

    try:
        studente = Studente("Paolo", "Bianchi", 17, "Ingegneria in Informatica", 27)
        print(studente)
        studente()
    
    except ValueError as e:
        print(f"Errore: {e}")
