# Hello Admin

list_usernames = ["admin", "vitto", "locopazzo", "pippo", "pluto", "niconicolino"]

specific_user = input("Inserire un username: ")

# for username in list_usernames:
#     if username == "admin":
#         print("Hello admin, would you like to see a status report?")
#     else:
#         print(f"Hello {username}, thank you for loggin in again.")

print("-" * 50)

# if specific_user in list_usernames:
#     if specific_user == "admin":
#         print("Hello admin, would you like to see a status report?")
#     else:
#         print(f"Hello {specific_user}, thank you for loggin in again.")
# else:
#     print(f"User \"{specific_user}\" not found.")

for specific_user in list_usernames:
    if specific_user == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {specific_user}, thank you for loggin in again.")