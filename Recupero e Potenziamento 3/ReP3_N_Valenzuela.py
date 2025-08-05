'''
Definire le seguenti classi con attributi privati:

A. Creatura con le seguenti proprietà:
- attributi: nome (di tipo stringa, per indicare il nome della creatura)
- metodi: tutti i metodi standard, ovvero __init__, setter, getter e __str__
In particolare:
il metodo setNome() deve fare un controllo se il nome inserito sia una stringa valida. 
In caso contrario, impostare il nome della creatura con il valore di "Creatura Generica".
il metodo __str__ deve mostrare in output: "Creatura: nome creatura"

B. Alieno (che eredita da Creatura) con le seguenti proprietà:
- attributi: matricola (di tipo intero positivo), munizioni (una lista di 15 interi positivi)
- metodi: setter, getter, __str__
In particolare:
il metodo setMatricola() (privato), non riceve argomenti in input e deve inizializzare l'attributo matricola 
con un numero intero positivo casuale tra 10000 e 90000.
Per generare un numero intero casuale nell'intervallo [a, b] (ovvero estremi inclusi), importare il modulo 
random e usare la funzione randint(a,b) del modulo;
 
Il metodo setMunizioni() (privato) non riceve argomenti in input e deve inizializzare l'attributo munizioni 
con una lista di 15 numeri interi positivi i cui elementi sono numeri della sequenza 0, 1, 4, 9, 16, 25, 36, 49, ... 
Usare le list comprehension.
il metodo __init__ deve inizializzare la superclasse, inizializzare la matricola e le munizioni.
Inoltre, i nomi di tutti gli alieni devono essere "Robot-" + matricola (ad esempio, "Robot-16326", 
scritto con la R maiuscola).
Pertanto, nel metodo __init__ impostare il nome dell'Alieno come richiesto, effettuando opportuni controlli. 
Nel caso in cui il nome dell'alieno non sia conforme, mostrare il seguente messaggio e re-impostare il nome in 
modo corretto: "Attenzione! Tutti gli Alieni devono avere il nome "Robot" seguito dal numero di matricola! 
Reimpostazione nome Alieno in Corso!".
il metodo __str__ deve mostrare in output: "Alieno: nome alieno" (ad esempio: Alieno: Robot-16326)

C. Mostro (che eredita da Creatura) con le seguenti proprietà:
- attributi: urlo_vittoria (di tipo stringa), gemito_sconfitta (di tipo stringa), assalto (una lista di 15 interi 
positivi)
- metodi: setter, getter, __str__
In particolare:
il metodo __init__ deve ricevere il nome del mostro, il suo urlo della vittoria ed il suo gemito sconfitta. 
Inoltre, deve inizializzare assalto.
il metodo setAssalto() (privato) non riceve argomenti in input e deve inizializzare l'attributo assalto con una 
lista di 15 numeri interi positivi casuali tra 1 e 100, estremi inclusi, tutti diversi tra loro.
i metodi setVittoria(vittoria: str) e setSconfitta(sconfitta: str) (privati), devono controllare se i valori di 
vittoria e sconfitta siano valori validi. In caso contrario, devono impostare gli attributi urlo_vittoria a 
"GRAAAHHH" e gemito sconfitta a "Uuurghhh".
ad esempio, se il nome del mostro è "Godzilla", il metodo __str__ dovrà mostrare a schermo: Mostro: gOdZiLlA, 
ovvero il nome del mostro scritto con i caratteri alternati minuscolo-maiuscolo.

---------------------------------------------------------------------------------------------------------------------------

1. All'interno del file ReP3_inizialeNome_Cognome (fuori dalla classi) definire le seguenti funzioni: pariUguali(a: list[int], b: list[int]). 
Questo metodo riceve in input due liste a e b di interi positivi e 
deve restituire una lista c.
Ogni elementi della lista c deve essere uguale a:
- 1 se l'elemento i-esimo di a e l'elemento i-esimo di b sono sono entrambi pari
- 0 altrimenti

2. combattimento(a: Alieno, m: Mostro). Questo metodo riceve in input un oggetto della classe Alieno ed un oggetto 
della classe Mostro. Il metodo deve controllare la validità di a e la validità di m. Se a non è un Alieno o se m 
non è un Mostro, il combattimento deve essere interrotto, mostrare un opportuno messaggio e ritornare None. 
Altrimenti, se a e m sono oggetti validi, il metodo deve simulare il combattimento tra Mostro e Alieno, 
restituendo la creatura vincitrice. Il combattimento consiste nell'applicare la funzione pariUguali() alle 
munizioni dell'Alieno e all'assalto del Mostro. Se la lista prodotta in output dal pariUguali() ha più di 4 elementi 
con valore 1, allora il vincitore è il mostro. Altrimenti, il vincitore è l'alieno. Se vince il mostro, sullo schermo 
viene stampato per 3 volte l'urlo della vittoria, altrimenti viene stampato il gemito della sconfitta.

3. proclamaVincitore(c: Creatura). Questo metodo stampa a schermo se hanno vinto gli alieni o i mostri 
(a seconda dell'oggetto c) e , mostra il vincitore all'interno di un rettangolo con contorno di * come nell'esempio.

*****************************

*                           *

*    Alieno: Robot-25855    *

*                           *

*****************************

*************************

*                       *

*    Mostro: gOrThOr    *

*                       *

*************************

Suggerimento: stampare prima il rettangolo vuoto, le cui dimensioni sono altezza 
5 e lunghezza = lunghezza di c.__str__() + 10
poi, modificare il codice in questo modo:
quando si arriva alla riga centrale del rettangolo (ovvero i=2), si deve stampare il nome del 
vincitore al centro del rettangolo.
per far questo si deve imporre la condizione i=2 e j =5. Se la condizione è verificata, stampare 
la creatura c (print(c), end=""), stampare 5 spazi vuoti e un * (print(     *), end="") e poi interrompere 
l'iterazione corrente.


Infine,
Scrivere nel metodo main, un codice Python che
- Inizializza un mostro e un alieno e stampa i dati corrispondenti sullo schermo.
- Esegue un combattimento tra i due oggetti creati.
- Proclama il vincitore.


Esempio di Output:

Alieno: Robot-41119
Munizioni: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]


Mostro: gOrThOr
Assalto: [13, 23, 28, 80, 50, 56, 33, 55, 15, 20, 15, 94, 42, 16, 46]

Combattimento

GRAAAHHH
GRAAAHHH
GRAAAHHH


I Mostri hanno vinto!

*************************

*                                    *

*    Mostro: gOrThOr    *

*                                    *

*************************
'''
from random import randint

class Creatura:

    def __init__(self, nome: str) -> None:
        self._nome = ""
        self.setnome(nome)

    def setnome(self, nome: str) -> None:
        if isinstance(nome, str) and nome.strip():
            self._nome = nome.strip()
        else:
            self._nome = "Creatura Generica"
    
    def getnome(self) -> str:
        return self._nome
    
    def __str__(self):
        return f"Creatura: {self._nome}"

class Alieno(Creatura):

    def __init__(self, nome: str) -> None:
        super().__init__(nome)
        self._matricola = self._setMatricola()
        self._munizioni = self._setMunizioni()

        nome_alieno = f"Robot-{self._matricola}"
        if self.getnome() != nome_alieno:
            print("Attenzione! Tutti gli Alieni devono avere il nome 'Robot' seguito dal numero di matricola!")
            print("\nReimpostazione nome Alieno in Corso...!\n")
            self.setnome(nome_alieno)

    def _setMatricola(self) -> int:

        self._matricola = randint(10000, 90000)
        return self._matricola
    
    def _setMunizioni(self) -> list[int]:
        self._munizioni = [i**2 for i in range(15)]
        return self._munizioni
    
    def getMatricola(self) -> int:
        return self._matricola
    
    def getMunizioni(self) -> list[int]:
        return self._munizioni
    
    def __str__(self) -> str:
        return f"Alieno: {self.getnome()}"

class Mostro(Creatura):

    def __init__(self, nome: str, urlo_vittoria: str, gemito_sconfitta: str, assalto: list[int] = None):
        super().__init__(nome)
        self._urlo_vittoria = ""
        self._gemito_sconfitta = ""
        self._setVittoria(urlo_vittoria)
        self._setSconfitta(gemito_sconfitta)

        if assalto is None:
            self._setAssalto()
        else:
            self._assalto = assalto
    
    def _setAssalto(self):
        self._assalto = [randint(1, 100) for _ in range(15)]
    
    def getAssalto(self):
        return self._assalto
    
    def geturloVittoria(self):
        return self._urlo_vittoria
    
    def getgemitoSconfitta(self):
        return self._gemito_sconfitta

    def _setVittoria(self, vittoria: str):
        if isinstance(vittoria, str) and vittoria.strip():
            self._urlo_vittoria = vittoria
        
        else:
            self._urlo_vittoria = "GRAAAHHHH"
    
    def _setSconfitta(self, sconfitta: str):
        if isinstance(sconfitta, str) and sconfitta.strip():
            self._gemito_sconfitta = sconfitta
        
        else:
            self._gemito_sconfitta = "Uuurghhh"
    
    def __str__(self):
        def crt_alternato(stringa: str):
            result = ""
            minuscola = True

            for carattere in stringa:

                if carattere.isalpha():
                    result += carattere.lower() if minuscola else carattere.upper()
                    minuscola = not minuscola
                else:
                    result += carattere

            return result
        
        return (f"Mostro: {crt_alternato(self.getnome())}")


def pariUguali(a: list[int], b: list[int]):
    c: list[int] = []

    lunghezza = min(len(a), len(b))

    for i in range(lunghezza):
        if a[i] % 2 == 0 and b[i] % 2 == 0:
            c.append(1)
        
        else:
            c.append(0)
    
    return c


def combattimento(a: Alieno, m: Mostro):
    if not isinstance(a, Alieno):
        print("Errore, l'oggetto 'a' non è un Alieno valido!")
        return None
    
    if not isinstance(m, Mostro):
        print("Errore, l'oggetto 'b' non è un Mostro valido!")
        return None
    
    print("Combattimento in corso...")
    munizioni = a.getMunizioni()
    assalto = m.getAssalto()

    risultato = pariUguali(munizioni, assalto)

    if risultato.count(1) > 4:
        print(f"{m.geturloVittoria()}\n" * 3)
        return m
    else:
        print(m.getgemitoSconfitta())
        return a
    

def proclamaVincitore(c: Creatura): 
    if not isinstance(c, Creatura):
        print("Errore, l'oggetto non è una Creatura valida!")
        return
    
    nome_vincitore = c.__str__()
    lunghezza = len(nome_vincitore) + 10 # lunghezza rettangolo
    altezza = 5 #altezza rettangolo

    # stampa del rettangolo vuoto
    for i in range(altezza):
        for j in range(lunghezza):
            if i == 0 or i == altezza - 1 or j == 0 or j == lunghezza - 1:
                print("*", end="")
            
            elif i == 2 and j == 5:
                print(c, end="")
                print(" " * 4, end="")
                print("*", end="")
                break
            else:
                print(" ", end="")
        print()  # nuova riga dopo ogni riga del rettangolo 


if __name__ == "__main__":
    # Creo un Alieno e un Mostro
    alieno = Alieno(nome=None)  # il nome verrà sovrascritto
    mostro = Mostro("Gorgoth", "GRAAAHHH", "Uuurghhh")

    print(alieno)
    print(f"Munizioni: {alieno.getMunizioni()}\n")

    print(mostro)
    print(f"Assalto: {mostro.getAssalto()}\n")

    vincitore = combattimento(alieno, mostro)

    if vincitore:
        proclamaVincitore(vincitore)

        

