from dottore import Dottore
from fattura import Fattura
from paziente import Paziente

# creazione dei 2 medici
medico1 = Dottore("Mario", "Rossi", "Cardiologo", 150.00)
medico2 = Dottore("Manuel", "Diaz", "Pediatra", 80.00)

# impostazione dell'età
medico1.eta = 50
medico2.eta = 40

# presentazione di ogni medico
medico1.doctorGreet()
print("-" * 35)
medico2.doctorGreet()

# creazione dei pazienti
pazienti_lista1 = [
    Paziente("Miguel", "Verdi", "A001"),
    Paziente("Anna", "Bianchi", "A002"),
    Paziente("Coni", "Ballarini", "A003"),
]

pazienti_lista2 = [
    Paziente("Nicolò", "Buonamico", "A025"),
]

# creazione delle fatture
fattura1 = Fattura(pazienti_lista1, medico1)
fattura2 = Fattura(pazienti_lista2, medico2)

# aggiorno salary iniziale
fattura1.getSalary()
fattura2.getSalary()

# salario di ogni dottore
print(f"Salario Dottore1: {fattura1.salary} euro")
print(f"Salario Dottore2: {fattura2.salary} euro")

# spostare paziente lista 1 a lista dei pazienti lista 2
paziente_da_spostare = pazienti_lista1[0]  # Primo paziente
fattura1.removePatient(paziente_da_spostare.idCode)
fattura2.addPatient(paziente_da_spostare)

# stampo salario
print(f"Salario Dottore1 dopo spostamento: {fattura1.salary} euro!")
print(f"Salario Dottore2 dopo spostamento: {fattura2.salary} euro!")

# --- Calcolo guadagno totale ospedale ---
totale_ospedale = 0
if fattura1.salary is not None:
    totale_ospedale += fattura1.salary
if fattura2.salary is not None:
    totale_ospedale += fattura2.salary

print(f"In totale, l'ospedale ha incassato: {totale_ospedale} euro!")