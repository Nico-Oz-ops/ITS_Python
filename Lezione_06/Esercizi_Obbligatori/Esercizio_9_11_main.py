from Esercizio_9_11 import User, Privilegi, Admin

user_1 = User("Toni", "Cienpesos", "tonnino", "toni19@gmail.com" )
privilegi_1 = Privilegi()
admin_1 = Admin(user_1, privilegi_1)

print(admin_1.describe_user())
print(admin_1.show_privileges())

