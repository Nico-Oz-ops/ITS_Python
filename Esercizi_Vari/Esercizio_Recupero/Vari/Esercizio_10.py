'''
Esercizio: Funzione check_traffic_light

Scrivi una funzione con il seguente header:

* check_traffic_light(red: bool, yellow: bool, green: bool) -> str


Descrizione:
La funzione prende tre parametri booleani che rappresentano lo stato di un semaforo:

    * red → rosso acceso
    * yellow → giallo acceso
    * green → verde acceso

La funzione deve ritornare:

    * "Fermati" se rosso è acceso o giallo è acceso
    * "Procedi" se verde è acceso e rosso e giallo sono spenti

Esempi:

check_traffic_light(True, False, False)   # "Fermati"
check_traffic_light(False, False, True)   # "Procedi"
check_traffic_light(False, True, True)    # "Fermati"

Vincolo:
Usare operatori logici (and, or, not) per determinare le condizioni; 
non usare condizioni predefinite o funzioni esterne.
'''
# Versione 1
def check_traffic_light(red: bool, yellow: bool, green: bool) -> str:
    if red or yellow:
        return "Fermati"
    elif green and not red and not yellow:
        return "Procedi"

# Versione 2
def check_traffic_light(red: bool, yellow: bool, green: bool) -> str:
    if red or yellow:
        return "Fermati"
    elif green:
        return "Procedi"