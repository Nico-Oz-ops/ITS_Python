# Glossary
Glossary:dict = {
    "lower":"it transforms every word in miniscule",
    "upper":"it transforms every work in capital letters",
    "title":"it transforms in capital letter every first letter of each word",
    "insert":"it allows to put a new element in the list",
    "append":"it allows to add a new element at the end of the list"
}

print("Glossary:\n")

print(f"lower:{Glossary['lower']}\n")
print(f"upper:{Glossary['upper']}\n")
print(f"title:{Glossary['title']}\n")
print(f"insert:{Glossary['insert']}\n")
print(f"append:{Glossary['append']}\n")           

for key in Glossary:
    Glossary[key] += "\n"

# for value in Glossary.values():
#     print(value)
