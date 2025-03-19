# Esercizio 02 - Automazione di un semaforo intelligente

veicoli_NS = int(input("Inserire il numero dei veicoli direzione Nord - Sud: "))
veicoli_EO = int(input("Inserire il numero dei veicoli direzione Est - Ovest: "))
soglia = 70

if veicoli_NS > soglia and veicoli_EO > soglia:
    tempo_NS = 50
    tempo_EO = 50
    print(f"Il tempo assegnato alla direzione Nord-Sud è {tempo_NS: .2f}%")
    print(f"Il tempo assegnato alla direzione Est-Ovest è {tempo_EO: .2f}%")

elif veicoli_NS > soglia:
    tempo_NS = 60
    tempo_EO = 40
    print(f"Il tempo assegnato alla direzione Nord-Sud è {tempo_NS: .2f}%")
    print(f"Il tempo assegnato alla direzione Est-Ovest è {tempo_EO: .2f}%")    

elif veicoli_EO > soglia:
    tempo_NS = 40
    tempo_EO = 60
    print(f"Il tempo assegnato alla direzione Nord-Sud è {tempo_NS: .2f}%")
    print(f"Il tempo assegnato alla direzione Est-Ovest è {tempo_EO: .2f}%")   

else:
    tempo_NS = (veicoli_NS / (veicoli_NS + veicoli_EO)) * 100
    tempo_EO = (veicoli_EO / (veicoli_NS + veicoli_EO)) * 100
    print(f"Il tempo assegnato alla direzione Nord-Sud è {tempo_NS: .2f}%")
    print(f"Il tempo assegnato alla direzione Est-Ovest è {tempo_EO: .2f}%")
