from forma_generica import FormaGenerica

class Rettangolo(FormaGenerica):

    # inizializzare un oggetto della classe Rettangolo
    def __init__(self):
        super().__init__()

        self.setShape('rettangolo')
    
    def draw(self) -> None:

        print(f"\n{self.getShape()}\n")

        # outer for

        for i in range(5):
            # inner for
            for j in range(5 * 2):

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




# triangolo

altezza = 5

for i in range(altezza):
    # Spazi iniziali per centrare il triangolo
    for j in range(altezza - i - 1):
        print(" ", end="")

    # Asterischi (lati e base)
    for k in range(2 * i + 1):
        print("*", end="")

    print()  # Vai a capo


altezza = 5

for i in range(altezza):
    for j in range(altezza - i - 1):
        print(" ", end="")

    for k in range(2 * i + 1):
        # Stampa asterisco solo ai bordi o alla base
        if k == 0 or k == 2 * i or i == altezza - 1:
            print("*", end="")
        else:
            print(" ", end="")

    print()

