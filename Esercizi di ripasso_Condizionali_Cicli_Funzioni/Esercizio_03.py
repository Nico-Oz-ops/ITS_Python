# Esercizio 3

def print_seq():
    print("Sequenza a): ")
    for i in range(1, 8):
        print(i)
    print()

    print("Sequenza b): ")
    for i in range(3, 24, 5):
        print(i)
    print()
    
    print("Sequenza c): ")
    for i in range(20, -11, -6):
        print(i)
    print()
    
    print("Sequenza d): ")
    for i in range(19, 52, 8):
        print(i)
   
    return

print_seq()




# def print_seq():
#     seqs = {
#         "Sequenza a": range(1, 8),
#         "Sequenza b": range(3, 24, 5),
#         "Sequenza c": range(20, -11, -6),
#         "Sequenza d": range(19, 52, 8)
#     }
#     for label, seq in seqs.items():
#         print(f"{label}):")
#         for num in seq:
#             print(num)

# print_seq()