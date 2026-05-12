# ### Parte 3: Modulo `playlist.py`
# Implementa funzioni per gestire collezioni di video.

# **Funzioni di base:**
# - `crea_playlist()` - crea un dizionario con nome e lista vuota di video
# - `aggiungi_video()` - aggiunge un video alla playlist
# - `rimuovi_video()` - rimuove un video per indice
# - `durata_totale()` - somma le durate di tutti i video
# - `dimensione_totale()` - somma le dimensioni di tutti i video
# - `mostra_playlist()` - formatta la playlist in una stringa leggibile

# **Funzioni di ordinamento (con sorted):**
# - `ordina_per_durata()` - ordina i video dal più breve al più lungo
#   - Usa `sorted()` con `key` per specificare quale attributo usare per l'ordinamento

# **Approfondimento: sorted() con key**
# `sorted()` ordina una lista. Normalmente ordina numeri e stringhe per valore naturale. Ma con `key`, puoi dire esattamente come confrontare gli elementi:
# - `key=lambda v: v["durata"]` ordina usando il valore della chiave "durata"


from .video_student import dimensione_video

def crea_playlist(nome:str) -> dict:
    return {"nome":nome, "video": []}

def aggiungi_video(playlist: dict, video: dict):
    playlist["video"].append(video)
    
def rimuovi_video(playlist: dict, indice: int):
    if 0 <= indice < len(playlist["video"]):
        del playlist["video"][indice]
    else:
        print("Indice non valido")
    
def durata_totale(playlist: dict) -> float:
    return sum(video["durata"] for video in playlist["video"])

def dimensione_totale(playlist: dict) -> float:
    return sum(dimensione_video(video) for video in playlist["video"])

def mostra_playlist(playlist: dict) -> str:
    return playlist


def ordina_per_durata(playlist: dict)-> str:
    playlist["video"] = sorted(playlist["video"], key=lambda v: v["durata"])
    return f"Playlist ordinata per durata: {playlist['video']}"
    


