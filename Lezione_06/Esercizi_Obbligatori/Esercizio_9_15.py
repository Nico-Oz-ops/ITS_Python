# Esercizio 9.15
'''
Analisi della lotteria: estendi la classe LotteryMachine creata nell'esercizio 9-14.

1. Aggiungere un metodo chiamato simulate_until_win(self, my_ticket) che:

Accetta un biglietto (un elenco di 4 elementi).
Estrae ripetutamente biglietti casuali utilizzando il  metodo draw_ticket() .
Tiene il conto di quanti tentativi sono necessari affinché un biglietto estratto a caso corrisponda  a my_ticket .
Restituisce il numero di tentativi e il biglietto vincente.

2. Crea un ticket denominato my_ticket con 4 numeri o lettere dal pool.

3. Utilizza il metodo simulate_until_win() per simulare quante estrazioni sarebbero necessarie affinché il 
tuo biglietto risultasse vincente.

4. Stampa un messaggio che mostra:

Il tuo biglietto
Il biglietto vincente
Quanti tentativi ci sono voluti per vincere
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
        print(f"Il mio biglietto è: {', '.join(self.my_ticket)}")
        print(f"Il biglietto vincente è: {', '.join(self.ticket_vincente)}")
    
    def simulate_until_win(self, my_ticket):
        # questo pezzo simula lìestrazione ripetuta di biglietti finché non si trova il bigliwetto vincente
        tentativi = 0

        while True:
            tentativi += 1
            self.selezioneTicketVincente()
            if sorted(self.ticket_vincente) == sorted(my_ticket):
                return tentativi, self.ticket_vincente
   
# ticket personalizzato
my_ticket = ["d", "1", "5", "a"]

# creo la macchina della lotteria
macchina_lotto = LotteryMachine()

# si esegue la simulazione fino a vincere
tentativi, ticket_vincente = macchina_lotto.simulate_until_win(my_ticket)

print(f"Il tuo biglietto: {my_ticket}")
print(f"Il biglietto vincente: {ticket_vincente}")
print(f"Ci sono voluti {tentativi} tentativi per vincere")
