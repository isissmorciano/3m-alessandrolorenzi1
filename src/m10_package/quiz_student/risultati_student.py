# ### Parte 3: Modulo `risultati.py`
# Funzioni per gestire i risultati del quiz e per salvarli/caricarli su file JSON:
# - `crea_risultati() -> dict:`
#   - Restituisce un dizionario con chiavi: `totale`, `corretti`
# - `registra_risposta(risultati: dict, corretta: bool) -> None:`
#   - Aggiorna i totali
# - `percentuale_corrette(risultati: dict) -> float:`
#   - Restituisce la percentuale di risposte corrette (1 decimale)
# - `mostra_risultati(risultati: dict) -> str:`
#   - Restituisce una stringa leggibile del riepilogo
# - `salva_risultati(risultati: dict, nome_file: str) -> None:`
#   - Salva i risultati in un file JSON
# - `carica_risultati(nome_file: str) -> dict:`
#   - Carica i risultati da un file JSON

import json

def crea_risultati()->dict:
    return {"totale":0,"corretti":0}


def registra_risposta(risultati: dict, corretta: bool) -> None:
    if corretta == True:
        risultati["totale"] += 1
        risultati["corretti"] += 1
    else:
        risultati["totale"] += 1


def percentuale_corrette(risultati: dict) -> float:
    percentuale = (risultati["corretti"]/risultati["totale"]) * 100
    return percentuale


def mostra_risultati(risultati: dict,percentuale:float) -> str:
    stringa = (f"Risultati:\nRisposte corrette: {risultati['corretti']}/{risultati['totale']} ({percentuale}%) ")
    return stringa


def salva_risultati(risultati: dict, nome_file: str) -> None:
    try:
        with open(nome_file,"w",encoding="utf-8") as file:
            json.dump(risultati,file,indent=4)
        print(f"File {nome_file} salvato con successo.")
    except IOError as e:
        print(f"Errore durante il salvataggio del file: {e}")


def carica_risultati(nome_file: str) -> dict:
    try:
        with open(nome_file,"r",encoding="utf-8") as file:
            risultati = json.load(file)
        return risultati
    except FileNotFoundError:
        print("Errore nella ricerca del file.")
        return {}
    except IOError as e:
        print(f"Errore del caricamento del file: {e}")
        return{}


