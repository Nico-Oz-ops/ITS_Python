'''Progettazione risorse: Considera un centro sportivo che gestisce corsi, istruttori e iscritti. 
Elenca le principali risorse e scrivi gli URI corretti. Indica anche esempi di URI errati.'''

'''
Risorse principali:
* Corsi (courses)
* Istruttori (instructors)
* Iscritti (members)

A. URI corretti(RESTful)

                                       --URI--
    - Tutti i corsi -->         /courses                      --> lista di tutti i corsi
    - Corso specifico -->       /courses/<course_id>          --> dettagli di un solo corso
    - Tutti gli istruttori -->  /instructors                  --> lista di tutti gli istruttori
    - Istruttore specifico -->  /instructors/<instructor_id>  --> dettagli di un solo istruttore
    - Tutti gli iscritti -->    /members                      --> lista di tutti gli iscritti
    - Iscritto specifico -->    /members/<member_id>          --> dettagli di un solo iscritto
    - Iscritto a un corso -->   /courses/<course_id>/members  --> lista iscritti a un solo corso
    


B. URI errati

    - /getAllCourses      --> contiene un verbo(get), non RESTful
    - /deleteInstructor/5 --> verbo nell'URI(delete), non RESTful
    - /members/list       --> /list è superfluo, basta solo scrivere /members che è già una lista degli iscritti
'''