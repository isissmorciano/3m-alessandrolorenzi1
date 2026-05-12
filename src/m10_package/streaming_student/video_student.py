# Parte 2: Modulo video.py
# Implementa funzioni per rappresentare e manipolare video come dizionari.

# Funzioni richieste:

# crea_video() - crea un dizionario video con: titolo, durata (secondi), risoluzione, bitrate (kbps)
# info_video() - formatta i dettagli del video in una stringa leggibile (es. "Titolo - M:SS - Risoluzione - Bitrate kbps")
# dimensione_video() - calcola la dimensione del file
# Approfondimento: Calcolo della dimensione Il bitrate è la quantità di dati trasmessi al secondo, misurata in kilobit per secondo (kbps). Per calcolare la dimensione di un file:

# Moltiplica la durata (in secondi) per il bitrate (in kbps) → ottieni kilobit totali
# Dividi per 8 per convertire kilobit in kilobyte
# Dividi per 1024 per convertire kilobyte in megabyte
# Arrotonda a 2 decimali
# Esempio: un video di 600 secondi a 5000 kbps occupa circa 366 MB


def crea_video(titolo:str,durata:float,risoluzione:str,bitrate:float)->dict:
    return {"titolo":titolo, "durata" : durata, "risoluzione":risoluzione, "bitrate":bitrate}


def info_video(video:dict) -> str:
    return (f"Titolo: {video['titolo']};\nDurata: {video['durata']};\nRisoluzione: {video['risoluzione']};\nBitrate: {video['bitrate']}")



def dimensione_video(video:dict) -> float:
    durata = video["durata"]
    bitrate = video["bitrate"]
    dimensione_kilobit = durata * bitrate
    dimensione_kilobyte = dimensione_kilobit / 8
    dimensione_megabyte = dimensione_kilobyte / 1024
    return round(dimensione_megabyte, 2)








