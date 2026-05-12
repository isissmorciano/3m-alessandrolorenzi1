# Parte 3: Implementazione di musica/playlist.py
# # Funzioni per gestire le playlist (liste di canzoni):

# # crea_playlist(nome: str) -> dict:
# # Restituisce un dizionario con nome e canzoni (lista vuota)
# # aggiungi_canzone(playlist: dict, canzone: dict) -> None:
# # Aggiunge una canzone alla playlist
# # rimuovi_canzone(playlist: dict, indice: int) -> None:
# # Rimuove una canzone per indice (0-based)
# # durata_totale(playlist: dict) -> int:
# # Restituisce durata totale in secondi
# # mostra_playlist(playlist: dict) -> str:
# # Restituisce stringa formattata con tutte le canzoni

def crea_playlist(nome:str) -> dict:
    return {"nome" : nome, "canzoni": []}


def aggiungi_canzone(playlist: dict, canzone_da_aggiungere: dict) -> None:
    playlist["canzoni"].append(canzone_da_aggiungere)
    print("Canzone aggiunta con successo! ")


def rimuovi_canzone(playlist: dict, canzone_da_rimuovere: str) -> None:
    for canzone in playlist["canzoni"]:
        if canzone == canzone_da_rimuovere:
            playlist["canzoni"].remove(canzone)
            print("Canzone rimossa con successo!")
        else:
            print("Nella playlist non è presente nessuna canzone con questo nome.")


def durata_totale(playlist: dict) -> int:
    durata_tot = 0
    for canzone in playlist["canzoni"]:
        durata_tot = durata_tot + canzone["durata"]
    return durata_tot


def mostra_playlist(playlist: dict) -> str:
    return(playlist)

