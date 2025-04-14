# Esercizio 9.14
'''
Lotteria: crea una classe LotteryMachine che contenga un elenco contenente una serie di 10 numeri e 5 lettere. 
Implementa un metodo per selezionare casualmente 4 elementi (numeri o lettere) da questo elenco per estrarre un 
biglietto vincente. Infine, implementa un metodo per visualizzare un messaggio che dice che qualsiasi biglietto 
che corrisponda ai 4 elementi vincenti vince un premio.
'''

import random

class LotteryMachine:

    def __init__(self):
        self.elementi = [str(elemento) for elemento in range(10)] + ["a", "b", "c", "d", "e"]
    
    def selezioneTicketVincente(self):
        self.ticket_vincente = random.sample(self.elementi, 4)
    
    def verifica_ticket(self, ticket):
        if sorted(ticket) == sorted(self.ticket_vincente):
            return "Hai vinto!"
        
        else:
            return "Buuuu, peccato hai perso :/"
    
    def visualizza_messaggio(self):
        print(f"I numeri vincenti sono: {', '.join(self.ticket_vincente)}")
        print("Qualsiasi biglietto che corrisponde ai 4 elementi vince un premio")

macchina_lotto = LotteryMachine()
macchina_lotto.selezioneTicketVincente()
macchina_lotto.visualizza_messaggio()

ticket = ["1", "10", "a", "c"]
print(macchina_lotto.verifica_ticket(ticket))


    

    
