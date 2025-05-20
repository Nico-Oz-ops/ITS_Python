from Persona import CodiceFiscale
from Persona import DataNascita
from Persona import Persona
from Uomo_Donna import Uomo
from Uomo_Donna import Donna
from Uomo_Donna import PosizioneMilitare
from Studente_Impiegato import Studente
from Studente_Impiegato import Impiegato
from Studente_Impiegato import Direttore
from Studente_Impiegato import Segretario
from Studente_Impiegato import Progettista
from Studente_Impiegato import Progetto

def test_creazione_persona():
    cod_fisc = CodiceFiscale("LZFSVT43D05H130C")
    data_nascita = DataNascita("29/08/1986")
    posizione_militare = PosizioneMilitare("Esente")

    uomo = Uomo("Clodoaldo", "Figliodipapà", data_nascita, cod_fisc, posizione_militare)
    
    print(uomo)
    print("-" * 50)

def test_studente():
    cod_fisc = CodiceFiscale("FNMLVZ27B58I290T")
    data_nascita = DataNascita("01/01/2006")

    studente = Studente("Lucasìn", "Buhaiolìn", data_nascita, cod_fisc, 123456789)
    print(studente)
    print("-" * 50)

def test_direttore():
    cod_fisc = CodiceFiscale("JTDVPR41E51G514L")
    data_nascita = DataNascita("30/06/1975")

    direttore = Direttore("Juanin", "Juanjarri", data_nascita, cod_fisc, 2750.00)
    print(direttore) 
    print("-" * 50)

def test_progettista():

    # Test Progettista-Progetto
    # Creazione di alcuni oggetti Progetto
    p1 = Progetto("Progetto A")
    p2 = Progetto("Progetto B")
    cod_fisc = CodiceFiscale("JTDVPR41E51G517B")
    data_nascita = DataNascita("30/06/1975")

    # Creazione di un oggetto Progettista con una lista di progetti
    progettista = Progettista("Giulia", "Verdi", data_nascita, cod_fisc, 2000.05, [p1, p2])

    # Verifica se il progettista ha progetti
    if progettista.haProgetti():
        print("Il progettista ha progetti!")
    else:
        print("Il progettista non ha progetti.")


if __name__ == "__main__":
    test_creazione_persona()
    test_studente()
    test_direttore()
    test_progettista()