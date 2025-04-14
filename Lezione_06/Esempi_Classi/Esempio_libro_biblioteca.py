class Libro:
    
    def __init__(self):
        self.titolo:str = ""
        self.autore:str = ""
        self.genere:list[str] = []
    
    def set_titolo(self,titolo_libro:str):
        self.titolo = titolo_libro
    
    def set_autore(self, nome_autore:str):
        self.autore = nome_autore
    
    def set_genere(self, lista_genere:list[str]):
        self.genere = lista_genere

    def get_titolo(self) -> str:
        return self.titolo 
    
    def get_autore(self) -> str:
        return self.autore
    
    def get_genere(self) -> list[str]:
        return self.genere

class Biblioteca:
    def __init__(self):
        self.libri:list[Libro] = []
    
    def set_libro(self, libro:Libro):
        self.libri.append(libro)
    
    def get_libri_titolo(self) -> str:
        for item in self.libri:
            print(item.get_titolo())

# oggetto vuoto
collezione:Biblioteca = Biblioteca()

print("Biblioteca creata")

# libro 1
piccolo_principe:Libro = Libro()
piccolo_principe.set_titolo("Il Piccolo Principe")
piccolo_principe.set_autore("Antoine de Saint-Exupéry")
piccolo_principe.set_genere(["Novella", "Favola"])

print(f"Titolo: {piccolo_principe.get_titolo()}\nAutore: {piccolo_principe.get_autore()}\nGenere: {piccolo_principe.get_genere()}")
print("-" * 50)

# libro 2
niebla:Libro = Libro()
niebla.set_titolo("Niebla")
niebla.set_autore("Miguel de Unamuno")
niebla.set_genere(["Romanzo"])

print(f"Titolo: {niebla.get_titolo()}\nAutore: {niebla.get_autore()}\nGenere: {niebla.get_genere()}")
print("-" * 50)

# Inserimento libro 1 e libro 2 nella biblioteca
collezione.set_libro(piccolo_principe)
collezione.set_libro(niebla)

print("Libri aggiunti alla collezione")
print("-" * 50)
collezione.get_libri_titolo()

test:Libro = Libro()
test.set_titolo("Harry Potter")
test.set_autore("JK Rowling")
test.set_genere(["Fantasy"])

collezione.set_libro(test)
print("-" * 50)
collezione.get_libri_titolo()



    



        