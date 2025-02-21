# More conditional tests

# equality and inequality with strings
print("EQUALITY AND INEQUALITY WITH STRINGS")

name = "Claire"

print("\nIs name == Claire? I predict True")
print(name == "Claire")

print("\nIs name != Cler? I predict is True")
print(name != "Cler")

print("\nIs name == Juan? I predict False")
print(name == "Juan")
print("-" * 50)

# using the lower() method
print("USING THE LOWER() METHOD")

color = "ReD"

print("\nIs color.lower() == red? I predict True")
print(color.lower() == "red")

print("\nIs color.lower() == ReD? I predict False")
print(color.lower() == "ReD")

print("\nIs color.lower() != blue? I predict True")
print(color.lower() != "blue")
print("-" * 50)

# numerical tests involving equality and inequality, 
# greater than and less than, greater than or equal to, and less than or equal to
print("NUMERICAL TESTS")

age_a = 18
age_b = 21
age_c = age_a

print("\nIs age_a == age_c? I predict True")
print(age_a == age_c)

print("\nIs age_a != age_b? I predict True")
print(age_a != age_b)

print("\nIs age_b == age_c? I predict False")
print(age_b == age_c)

print("\nIs age_c > age_a? I predict False")
print(age_c > age_a)

print("\nIs age_a < age_b? I predict True")
print(age_a < age_b)

print("\nIs age_b <= age_c? I predict False")
print(age_b <= age_c)

print("\nIs age_c >= age_a? I predict True")
print(age_c >= age_a)
print("-" * 50)

# tests using the and keyword and the or keyword
print("TESTS USING THE AND KEYWORD AND THE OR KEYWORD")

x = 71
y = 69

print("\nIs x < 100 and y < 70? I predict True")
print(x < 100 and y < 70)

print("\nIs x < y and y > 70? I predict False")
print(x < y and y > 70)

print("\nIs x > y and y > 69.5? I predict False")
print(x < y and y > 69.5)

print("\nIs x > 75 or y < x? I predict True")
print(x > 75 or y < x)

print("\nIs x < y or y > (x + y) ? I predict False")
print(x < y or y > (x + y))
print("-" * 50)

# test whether an item is in a list
print("TEST WHETHER AN ITEM IS IN A LIST")

list_spesa = ["avena", "petto di pollo", "latte scremato", "uova"]

print("\nIs 'avena' in list_spesa? I predict True")
print("avena" in list_spesa)

print("\nIs 'latte intero' in list_spesa? I predict False")
print("latte intero" in list_spesa)
print("-" * 50)

# test whether an item is not in a list
print("TEST WHETHER AN ITEM IS NOT IN A LIST")

print("\nIs 'uova' not in list_spesa? I predict False")
print("uova" not in list_spesa)

print("\nIs 'ketchup' not in list_spesa? I predict True")
print("ketchup" not in list_spesa)