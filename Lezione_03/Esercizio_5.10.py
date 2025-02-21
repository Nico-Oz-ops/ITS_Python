# Checking usernames

current_users = ["kIKo", "sAKi", "jugo", "maki", "niko"]
new_users = ["lizard", "mOKo", "kiko", "saki", "telo"]

current_users_lower = [user.lower() for user in current_users]

for user in new_users:
    if user.lower() in current_users_lower:
        print(f"The username \"{user}\" is already exists. Please enter a new username.")
    else:
        print(f"Super! \"{user}\" is available.")


# for user in new_users:
#     if user in current_users:
#         print(f"The username \"{user}\" is already exists. Please enter a new username.")
#     else:
#         print(f"Super! \"{user}\" is available.")

