'''
Esercizio: Analisi dei voti degli studenti

Scrivi una funzione con il seguente header:
    * analyze_grades(grades: list[float]) -> dict[str, float]

che, data una lista di voti compresi tra 0 e 10, ritorni un dizionario con le seguenti chiavi:

    * "highest" → il voto più alto nella lista
    * "lowest" → il voto più basso nella lista
    * "range" → la differenza tra voto massimo e voto minimo
    * "average" → la media aritmetica dei voti

Vincoli:
    * Non puoi usare funzioni built-in come min(), max(), sum() o librerie esterne.
    * Se la lista è vuota, la funzione deve sollevare un ValueError con il messaggio "lista vuota".
'''

def analyze_grades(grades: list[float]) -> dict[str, float]:
    if not grades:
        raise ValueError("Lista vuota")
    
    voto_alto = grades[0]
    voto_basso = grades[0]
    somma_voto = 0

    for voto in grades:
        if voto > voto_alto:
            voto_alto = voto
        
        elif voto < voto_basso:
            voto_basso = voto
        
        somma_voto += voto
    
    media_voto = somma_voto / len(grades)
    range_max_min = voto_alto - voto_basso

    return {"highest": voto_alto,
            "lowest": voto_basso,
            "range": range_max_min,
            "average": media_voto}
    


voti = [6.5, 8.0, 7.2, 9.5, 5.0]
print(analyze_grades(voti))