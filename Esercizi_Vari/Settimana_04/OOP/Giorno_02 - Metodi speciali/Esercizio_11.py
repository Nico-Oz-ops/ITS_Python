'''
11. Classe Rubrica con contatti unici

Tema: __init__, __str__, __len__, __eq__

Obiettivo: Lista di contatti senza duplicati

Traccia:
Crea una classe Rubrica con attributo lista di contatti (ogni contatto ha nome e numero).

    * __str__ → "Rubrica: nome1, nome2, …"
    * __len__ → numero di contatti
    * __eq__ → due rubriche uguali se contengono gli stessi contatti
'''
class Contatto:
    def __init__(self, nome: str, numero: str):
        self.nome = nome
        self.numero = numero
    
    def __str__(self):
        return f"Nome: {self.nome} - Telefono: {self.numero}"
    
    def __eq__(self, other):
        if not isinstance(other, Contatto):
            return NotImplemented
        
        return (self.nome, self.numero) == (other.nome, other.numero)
    
    def __lt__(self, other):
        # un contatto è “minore” di un altro se il nome è alfabeticamente prima, 
        # o se i nomi sono uguali, il numero è minore. Così Python saprà come ordinare
        return (self.nome, self.numero) < (other.nome, other.numero)

class Rubrica:
    def __init__(self, contatti: list[Contatto] = None):
        self.contatti = contatti if contatti is not None else []
    
    def aggiungi_contatto(self, contatto: Contatto):
        if not isinstance(contatto, Contatto):
            raise ValueError ("Errore, contatto non valido")
        self.contatti.append(contatto)
    
    def rimuove_contatto(self, contatto: Contatto):
        if contatto not in self.contatti:
            raise ValueError (f"Il contatto '{contatto}' non esiste.")
        self.contatti.remove(contatto)
    
    def __len__(self):
        return len(self.contatti)
    
    def __str__(self):
        contatto_str = ", ".join(str(contatto) for contatto in self.contatti)
        return f"Rubrica\n{contatto_str}\nContatti totali: {len(self.contatti)}"
    
    def __eq__(self, other):
        if not isinstance(other, Rubrica):
            return NotImplemented
        
        return sorted(self.contatti) == sorted(other.contatti)


contatto1 = Contatto("Nico", "125478")
contatto2 = Contatto("Javi", "369159")
contatto3 = Contatto("Benja", "741852")
contatto4 = Contatto("Manuele", "456987")
contatto5 = Contatto("Carlo", "759844")

rubrica1 = Rubrica([])
rubrica2 = Rubrica([])
print(rubrica1)
print("--------")
print(rubrica2)
rubrica1.aggiungi_contatto(contatto1)
rubrica1.aggiungi_contatto(contatto3)
print(rubrica1)
rubrica2.aggiungi_contatto(contatto2)
rubrica2.aggiungi_contatto(contatto5)
print(rubrica2)
rubrica1.rimuove_contatto(contatto3)
print(rubrica1)
print(rubrica2)
print(rubrica1 == rubrica2)


# Versione suggerita da Chat

class Contatto:
    def __init__(self, nome: str, numero: str):
        self.nome = nome
        self.numero = numero
    
    def __str__(self):
        return f"{self.nome} - {self.numero}"
    
    def __eq__(self, other):
        if not isinstance(other, Contatto):
            return NotImplemented
        return (self.nome, self.numero) == (other.nome, other.numero)
    
    def __hash__(self):
        return hash((self.nome, self.numero))


class Rubrica:
    def __init__(self, contatti: list[Contatto] = None):
        self.contatti = contatti if contatti is not None else []
    
    def aggiungi_contatto(self, contatto: Contatto):
        if not isinstance(contatto, Contatto):
            raise ValueError("Errore, contatto non valido")
        self.contatti.append(contatto)
    
    def rimuove_contatto(self, contatto: Contatto):
        if contatto not in self.contatti:
            raise ValueError(f"Il contatto '{contatto}' non esiste.")
        self.contatti.remove(contatto)
    
    def cerca_per_nome(self, nome: str):
        return [c for c in self.contatti if c.nome.lower() == nome.lower()]
    
    def __len__(self):
        return len(self.contatti)
    
    def __contains__(self, contatto: Contatto):
        return contatto in self.contatti
    
    def __str__(self):
        contatti_str = "\n".join(str(c) for c in self.contatti)
        return f"Rubrica:\n{contatti_str}\nTotale contatti: {len(self.contatti)}"
    
    def __eq__(self, other):
        if not isinstance(other, Rubrica):
            return NotImplemented
        # Confronto ignorando l'ordine dei contatti
        return sorted(self.contatti, key=lambda c: (c.nome, c.numero)) == sorted(other.contatti, key=lambda c: (c.nome, c.numero))


'''
Novità rispetto alla tua versione:

1. __hash__ in Contatto → permette di usare i contatti in set o come chiavi di dizionario.
2. cerca_per_nome → restituisce tutti i contatti che corrispondono al nome, case-insensitive.
3. __contains__ → permette di fare if contatto in rubrica.
4. __eq__ → ora confronta le rubriche ignorando l’ordine dei contatti.
5. rimuove_contatto → solleva eccezione se il contatto non esiste, più Pythonico.
6. __str__ → stampa ogni contatto su una riga separata.


Per poter confrontare due rubriche in modo corretto, Python deve sapere come confrontare gli oggetti contenuti nelle liste, cioè i Contatto.

Quindi:

Rubrica.__eq__ confronta le liste di contatti (self.contatti == other.contatti).
Contatto.__eq__ dice a Python quando due contatti sono uguali.
Senza Contatto.__eq__, il confronto tra rubriche avrebbe confrontato solo l’identità 
degli oggetti (quelli in memoria), e due contatti con stesso nome/numero ma oggetti 
diversi sarebbero stati considerati diversi.

In breve: Rubrica confronta le liste → Contatto confronta gli elementi.
'''
