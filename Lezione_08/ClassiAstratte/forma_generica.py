from abc import ABC, abstractmethod

# classe Forma Generica astratta
class FormaGenerica(ABC):
    
    # metodo astratto della classe Forma Generica
    @abstractmethod 
    def draw(self) -> None:
        pass

    def setShape(self, shape:str) -> None:
        if not isinstance(shape, str) or shape.strip() == "":
            raise ValueError("\nErrore! 'Shape' deve essere una stringa, e non deve essere vuota")
        
        else:
            self.shape = shape
    
    def getShape(self) -> str:
        return self.shape

class Rettangolo(FormaGenerica):

    # inizializzare un oggetto della classe Rettangolo
    def __init__(self):
        super().__init__()

        self.setShape("Questa è la forma di un rettangolo:")
    
    def draw(self) -> None:

        print(f"\n{self.getShape()}\n")

        # outer for

        for i in range(5):
            # inner for
            for j in range(10):

                # lato a e lato d del rettangolo
                if i == 0 or i == 5 - 1:
                    print("*", end=" ")
                
                # lato b e lato c del rettangolo
                elif j == 0 or j == (5 * 2) - 1:
                    print("*", end=" ")
                    # stampa gli spazi bianchi
                else:
                    print(" ", end=" ")

            print("\n", end="")

# creo un oggetto 'r' della classe Rettangolo
r: Rettangolo = Rettangolo()
r.draw()


class Cerchio(FormaGenerica):

    # inizializzare un oggetto della classe Cerchio
    def __init__(self):
        super().__init__()

        self.setShape("Questa è la forma di un cerchio:")
    
    def draw(self) -> None:

        print(f"\n{self.getShape()}\n")

        # outer for

        radius = 10

        for y in range(-radius, radius + 1):
            for x in range(-radius, radius + 1):

                # Calcolo distanza dal centro (0,0)

                if radius**2 - 5<= x**2 + y**2 <= radius**2 + 5:
                    print("*", end=" ")

                else:
                    print(" ", end=" ")
            print()

# creo un oggetto 'c' della classe Cerchio
c: Cerchio = Cerchio()
c.draw()






