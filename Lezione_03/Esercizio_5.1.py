# Conditional test

# Tests evaluate to True
car = "nissan"
print("TESTS EVALUATE TO TRUE")
print("\nIs car == \"nissan\"? I predict True")
print(car == "nissan")

print("\nIs car != \"toyota\"? I predict True")
print(car != "toyota")

print("\nIs car.lower() == \"nissan\"? I predict True")
print(car.lower() == "nissan")

print("\nIs 's' in car? I predict True")
print("s" in car)

print("\nIs len(car) = 6? I predict True")
print(len(car) == 6)
print("-" * 50)
# Tests evaluate to False
print("TESTS EVALUATE TO FALSE")
print("\nIs car == \"audi\"? I predict False")
print(car == "audi")

print("\nIs car != \"nissan\"? I predict False")
print(car != "nissan")

print("\nIs car.upper() == \"nissan\"? I predict False")
print(car.upper() == "nissan")

print("\nIs 'e' in car? I predict False")
print("e" in car)

print("\nIs len(car) == 4? I predict False")
print(len(car) == 4)
