'''
    * Un decorator @ è una funzione che espande il funzionamento di un'altra funzione


    * Un decoratore in Python (quello con la @) è una funzione speciale che "espande" o 
    modifica il comportamento di un’altra funzione, senza modificarne direttamente il codice.


    * Un decoratore è una funzione che prende un’altra funzione come argomento, e restituisce 
    una nuova funzione, solitamente con comportamento modificato o esteso.
'''

# Esempio 1
'''
* Il wrapper wrapper() non accetta argomenti.
* Può decorare solo funzioni senza parametri, altrimenti si genera un errore.
'''
def cronometro(fun):
    def wrapper():
        import time 
        start = time.time()
        fun()
        print(time.time() - start)
    return wrapper

@cronometro
def prova():
    for i in range(1000000):
        pass
prova()

# Esempio 2
'''
* Il wrapper wrapper1(*args) accetta un numero variabile di argomenti.

* Può decorare funzioni con uno o più parametri, rendendolo più generico e riutilizzabile.
'''
def cronometro1(fun):
    def wrapper1(*args): #in questa maniera posso passare una quantità X di parametri
        import time 
        start = time.time()
        fun(*args)
        print(time.time() - start)
    return wrapper1

@cronometro1
def prova1():
    for i in range(1000000):
        pass
prova1()

