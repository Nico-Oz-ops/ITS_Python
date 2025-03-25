class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __repr__(self):
        return f"{self.name}, {self.age}"

alice = Person("Alice W.", 45)
bob = Person("Bob M.", 36)

print(f"Età di Bob: {bob.age} anni")

if bob.age > alice.age:
    print("Bob è più vecchio di Alice")
else:
    print("Alice è più vecchia di Bob")

nico = Person("Nico V.", 36)
lisa = Person("Lisa B.", 26)
dendè = Person("Dendè S.", 279)

people = [nico, lisa, dendè, alice, bob]

youngest_person = people[0]

for person in people:
    if person.age < youngest_person.age:
        youngest_person = person

print(f"La persona più giovane è {youngest_person}")

