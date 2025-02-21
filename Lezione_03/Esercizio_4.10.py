list_cube = [cube ** 3 for cube in range(1, 11)]
print(list_cube)
first_three = print(f"The first three items in the list are: {list_cube[:3]}")

middle = len(list_cube) // 2
print(middle)
middle_three = print(f"Three items from the middle of the list are: {list_cube[middle:middle + 3]} ")
last_three = print(f"The last three items in the list are: {list_cube[-3:]}")
