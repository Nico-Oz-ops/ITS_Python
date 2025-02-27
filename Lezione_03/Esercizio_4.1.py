# Opzione 1 - Ciclo For

# favorite_pizza = ["Margherita", "Diavola", "'Nduja"]

# for pizza in favorite_pizza:
#     # print(pizza)
#     print(f"I like {pizza} pizza")
# print("I love pizza! Frickin' so much")


# Opzione 2 - Ciclo While

favorite_pizza_2 = []
i = 1

while i <= 3:
    pizza = input(f"Inserire la tua {i}a pizza favorita: ").lower()
    favorite_pizza_2.append(pizza)
    i += 1
    print(f"Mi piace tanto la pizza, soprattutto: {pizza}")
print(f"Le mie pizza favorite sono: {favorite_pizza_2}")



