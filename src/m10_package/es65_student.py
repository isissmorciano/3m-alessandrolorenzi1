from diario_student import entrate_student,persistenza_student


def main():
    e1 = entrate_student.crea_entrata("2026-04-08","Ho iniziato un nuovo corso python","studio",60)
    e2 = entrate_student.crea_entrata("2026-04-08","Ho scritto un esercizio sul package diario.","studio",45)
    e3 = entrate_student.crea_entrata("2026-04-09","Sono andato a fare una passeggiata nel bosco","tempo libero",30)
    mio_diario = entrate_student.crea_diario()
    entrate_student.aggiungi_entrata(mio_diario,e1)
    entrate_student.aggiungi_entrata(mio_diario,e2)
    entrate_student.aggiungi_entrata(mio_diario,e3)
    print("--------Diario--------")
    # for entrata in mio_diario["entrate"]:
    print(f"\n{entrate_student.info_entrata(e1)}")
    print(f"\n{entrate_student.info_entrata(e2)}")
    print(f"\n{entrate_student.info_entrata(e3)}")
    print(f"\nTempo totale: {entrate_student.tempo_totale(mio_diario)}")
    # print(f"\nTempo per categoria:\n{entrate_student.tempo_per_categoria(mio_diario)}")
    nome_file = "diario.json"
    persistenza_student.salva_diario(mio_diario,nome_file)
    # risultati_caricati = persistenza_student.carica_diario(nome_file)
    # print(f"Risultati caricati:\n{risultati_caricati}")

if __name__ == "__main__":
    main()
