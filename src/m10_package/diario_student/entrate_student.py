def crea_entrata(data: str, testo: str, categoria: str, durata: int) -> dict:
    return {"data":data,"testo":testo,"categoria":categoria,"durata":durata}


def info_entrata(entrata: dict) -> str:
    stringa = f"Data:{entrata['data']}\nCategoria:{entrata['categoria']}\nDurata:{entrata['durata']}\nTesto:{entrata['testo']}"
    return stringa


def crea_diario() -> dict:
    return {"entrate":[]}

def aggiungi_entrata(diario: dict, entrata_da_aggiungere: dict) -> None:
    diario["entrate"].append(entrata_da_aggiungere)
    


def rimuovi_entrata(diario: dict, indice: int) -> None:
    if 0 <= indice < len(diario["entrate"]):
        diario["entrate"].pop(indice)
    else:
        print(f"Errore: indice {indice} non valido")


def tempo_totale(diario: dict) -> int:
    totale = 0
    for entrata in diario["entrate"]:
        totale = totale + entrata["durata"]
    return totale


def tempo_per_categoria(diario: dict) -> dict[str, int]:
    pass 

def trova_entrate_per_data(diario: dict, data: str) -> list[dict]:
    entrate_trovate = []
    for entrata in diario["entrate"]:
        if data == entrata["data"]:
            entrate_trovate.append(entrata)
    return entrate_trovate          
      



    
        
        
    

    
