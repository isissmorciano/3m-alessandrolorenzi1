import json
def salva_diario(diario: dict, nome_file: str) -> None:
    try:
        with open(nome_file,"w",encoding="utf-8") as file:
            json.dump(diario,file,indent=4)
        print(f"File {nome_file} salvato con successo!")
    except IOError as e:
        print(f"Errore durante il salvataggio del file: {e}")


def carica_diario(nome_file: str) -> dict:
    try:
        with open(nome_file,"r",encoding="utf-8") as file:
            diario = json.load(file)
        return diario
    except FileExistsError:
        print("Errore nella ricerca del file.")
        return {}
    except IOError as e:
        print(f"Errore nel caricamento del file: {e}")
        return{}


