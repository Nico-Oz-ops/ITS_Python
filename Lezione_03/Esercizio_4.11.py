# My pizzas, your pizzas

favorite_pizza = ["Margherita", "Diavola", "'Nduja"]

friend_pizzas = favorite_pizza[:]

favorite_pizza.append("Quattro Stagioni")
friend_pizzas.append("Capricciosa")

print("My favorite pizzas are:")
for pizza in favorite_pizza:
    print(pizza)

print("-" * 35)

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)