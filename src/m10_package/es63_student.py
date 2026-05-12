# ### Parte 4: Dati da usare

# **Nome playlist:** `"Corso Python Base"`

# **Video da aggiungere (nell'ordine):**

# | Titolo | Durata (s) | Risoluzione | Bitrate (kbps) |
# |--------|-----------|-------------|---|
# | Introduzione a Python | 930 | 1080p | 5000 |
# | Variabili e Tipi | 1335 | 720p | 3000 |
# | Funzioni e Moduli | 1080 | 1080p | 5000 |
# | Liste e Dizionari | 1560 | 480p | 2000 |

# ### Parte 5: Utilizzo del Package
# Scrivi uno script che:
# 1. Importa il package
# 2. Crea una playlist con il nome specificato
# 3. Aggiunge i 4 video con i dati della tabella sopra
# 4. Stampa la playlist originale
# 5. Stampa la playlist ordinata per durata
# 6. Stampa statistiche totali (durata e dimensione)



from streaming_student.video_student import crea_video
from streaming_student.playlist_video_student import crea_playlist, aggiungi_video, mostra_playlist, ordina_per_durata, durata_totale, dimensione_totale


def main():
    nome = "Corso Python Base"
    playlist = crea_playlist(nome)
    
    v1 = crea_video("Introduzione a python",930,"1080p",5000)
    v2 = crea_video("variabili e Tipi",1335,"720p",3000)
    v3 = crea_video("Funzioni e Moduli",1080,"1080p",5000)
    v4 = crea_video("Liste e Dizionari",1560,"480p",2000)
    
    aggiungi_video(playlist,v1)
    aggiungi_video(playlist,v2)
    aggiungi_video(playlist,v3)
    aggiungi_video(playlist,v4)
    print(f"La playlist originale è :\n{mostra_playlist(playlist)}")
    print(f"La playlist ordinata per durata è: {ordina_per_durata(playlist)}")
    print(f"La durata totale della playlist è: {durata_totale(playlist)} secondi")
    print(f"{dimensione_totale(playlist)} MB")


if __name__ == "__main__":
    main()