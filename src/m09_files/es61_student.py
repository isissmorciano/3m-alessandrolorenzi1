# Esercizio 61: Package "Musicale" - Canzoni e Playlist
# Obiettivo
# Creare un package musica che gestisca canzoni e playlist con funzioni pure.

# Istruzioni
# Parte 1: Creazione della struttura del package
# Crea una cartella musica/ con:

# musica/
# ├── __init__.py
# ├── canzoni.py
# └── playlist.py
# Parte 2: Implementazione di musica/canzoni.py
# Funzioni per gestire le canzoni (rappresentate come dizionari):

# crea_canzone(titolo: str, artista: str, durata: int) -> dict:
# Restituisce un dizionario con chiavi: titolo, artista, durata
# info_canzone(canzone: dict) -> str:
# Restituisce formato: "Titolo - Artista (M:SS)"
# Esempio: "Bohemian Rhapsody - Queen (5:55)"
# Parte 3: Implementazione di musica/playlist.py
# Funzioni per gestire le playlist (liste di canzoni):

# crea_playlist(nome: str) -> dict:
# Restituisce un dizionario con nome e canzoni (lista vuota)
# aggiungi_canzone(playlist: dict, canzone: dict) -> None:
# Aggiunge una canzone alla playlist
# rimuovi_canzone(playlist: dict, indice: int) -> None:
# Rimuove una canzone per indice (0-based)
# durata_totale(playlist: dict) -> int:
# Restituisce durata totale in secondi
# mostra_playlist(playlist: dict) -> str:
# Restituisce stringa formattata con tutte le canzoni
# Parte 4: Utilizzo del package in es51_main.py
# Crea una playlist con nome a scelta
# Crea almeno 3 canzoni
# Aggiungile alla playlist
# Stampa il contenuto con durata totale
# Concetti Chiave
# Package: cartella con __init__.py e moduli
# Moduli correlati: canzoni.py e playlist.py lavorano insieme
# Funzioni pure: niente classi, solo funzioni che lavorano con dizionari
# Dizionari: strutture dati per rappresentare dati
# Esempio di Output
# === Playlist: Le mie canzoni preferite ===
# 1. Bohemian Rhapsody - Queen (5:55)
# 2. Stairway to Heaven - Led Zeppelin (8:02)
# 3. Hotel California - Eagles (6:30)

# Durata totale: 20:27
# Suggerimenti
# Rappresenta una canzone con: {"titolo": "...", "artista": "...", "durata": 355}
# Rappresenta una playlist con: {"nome": "...", "canzoni": [...]}
# Converti secondi in M:SS con: minuti = durata // 60, secondi = durata % 60



# Parte 4: Utilizzo del package in es51_main.py
# # Crea una playlist con nome a scelta
# # Crea almeno 3 canzoni
# # Aggiungile alla playlist
# # Stampa il contenuto con durata totale
from musica import playlist,canzoni
def main()->None:
    nome = input("Insersci il nome della tua nuova playlist: ")
    mia_playlist = playlist.crea_playlist(nome)
    for _ in range(3):
        titolo = input("Inserisci il titolo di una canzone: ")
        artista = input("Inserisci l'artista della canzone: ")
        durata = int(input("Quanto dura questa canzone: "))
        mia_canzone = canzoni.crea_canzone(titolo,artista,durata)
        mia_playlist["canzoni"].append(mia_canzone)
    for canzone in mia_playlist["canzoni"]:
        print(f"{canzoni.info_canzone(canzone)}")
    while True:
        print("Scegli cosa vuoi fare:")
        print("1 - Aggiungi una canzone alla playlist.")
        print("2 - Rimuovi una canzone dalla playlist.")
        print("3 - Visualizza la durata totale della playlist.")
        print("4 - Visualizza la playlist: ")
        print("5 - Esci")
        scelta = int(input("Inserisci una scelta 1-5: "))
        if scelta == 1:
            titolo = input("Inserisci il titolo di una canzone da aggiungere alla playlist: ")
            artista = input("Inserisci l'artista della canzone da aggiungere alla playlist: ")
            durata = int(input("Inserisci la durata della canzone da aggiungere alla playlist: "))
            canzone_da_aggiungere = canzoni.crea_canzone(titolo,artista,durata)
            playlist.aggiungi_canzone(mia_playlist,canzone_da_aggiungere)
        elif scelta == 2:
            titolo = input("Inserisci il titolo di una canzone da rimuovere dalla playlist: ")
            artista = input("Inserisci l'artista della canzone da rimuovere dalla playlist: ")
            durata = int(input("Inserisci la durata della canzone da rimuovere dalla playlist: "))
            canzone_da_rimuovere = canzoni.crea_canzone(titolo,artista,durata)
            playlist.rimuovi_canzone(mia_playlist,canzone_da_rimuovere)
        elif scelta == 3:
            durata_tot = playlist.durata_totale(mia_playlist)
            print(f"La playlist {mia_playlist} dura {durata_tot}")
        elif scelta == 4:
            print(f"{mia_playlist} : {playlist.mostra_playlist(mia_playlist)}")
        elif scelta == 5:
            print("Sei uscito con successo!")
            break
if __name__ == "__main__":
    main()



        