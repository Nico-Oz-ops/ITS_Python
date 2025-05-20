# Esercizio 4
'''
Scrivi una funzione che prenda in input una lista di dizionari 
che rappresentano voti di studenti e aggrega i voti per studente in un nuovo dizionario.
'''

def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:
    voti_studente = {}

    for dizionario in voti:

        nome = dizionario["nome"]
        voto = dizionario["voto"]

        if nome not in voti_studente:
            voti_studente[nome] = []
        voti_studente[nome].append(voto)
    
    return voti_studente


print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}]))
print(aggrega_voti([{'nome': 'Bob', 'voto': 75}, {'nome': 'Bob', 'voto': 85}]))
print(aggrega_voti([{'nome': 'Carl', 'voto': 60}, {'nome': 'Carl', 'voto': 70}, {'nome': 'Carl', 'voto': 80}]))
print(aggrega_voti([]))