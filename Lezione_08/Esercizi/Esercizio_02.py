# Esercizio 02

'''
Esercizio 2: Implementazione di metodi statici
Crea una classe chiamata MathOperations per raggruppare alcune funzionalità aritmetiche di base. 
All'interno di questa classe, definisci due metodi statici:

 *  add, che accetta due parametri numerici e restituisce la loro somma.

 *  multiply, che accetta anch'essa due parametri numerici e restituisce il loro prodotto.

Infine , scrivi un piccolo programma driver per testare la funzionalità dei metodi add e multiply. 
Questo dovrebbe comportare la chiamata di entrambi i metodi con input di esempio e la stampa dei risultati 
per verificarne il corretto funzionamento.
'''

class MathOperations:

    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b
    
    @staticmethod
    def multiply(a: float, b: float) -> float:
        return a * b


def main():

    print("Somma")
    print(f"5 + 4 = {MathOperations.add(5, 4)}")

    print("Moltiplicazione")
    print(f"7 * 4 = {MathOperations.multiply(7, 4)}")

if __name__ == "__main__":
    main()