from quiz_student import domande_student
from quiz_student import risultati_student  


def main()->None:
    q1 = domande_student.crea_domanda(
        "Qual è il linguaggio usato in questo corso?",
        ["Python", "Java", "C++"],
        0,
    )
    q2 = domande_student.crea_domanda(
        "Quale struttura dati Python usa parentesi quadre?",
        ["Dizionario", "Lista", "Tupla"],
        1,
    )
    q3 = domande_student.crea_domanda(
        "Quale comando usi per stampare in Python?",
        ["print", "echo", "console.log"],
        0,
    )

    domande_quiz = [q1,q2,q3]
    risposte_utente =[0,1,0]
    risultati = risultati_student.crea_risultati()
    
    for domanda, scelta in zip(domande_quiz, risposte_utente):
        corretta = domande_student.verifica_risposta(domanda, scelta)
        risultati_student.registra_risposta(risultati, corretta)
        
    percentuale = risultati_student.percentuale_corrette(risultati)
    stampa = risultati_student.mostra_risultati(risultati,percentuale)
    print(f"{stampa}\n")
    nome_file = "risultati.json"
    risultati_student.salva_risultati(risultati,nome_file)
    risultati_caricati = risultati_student.carica_risultati(nome_file)
    print(f"Risultati caricati:\n{risultati_caricati}")
    
if __name__ == "__main__":
    main()
    