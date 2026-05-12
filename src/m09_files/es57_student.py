# # Esercizio 57: Conteggio Parole in un File

# ## Obiettivo
# Leggere un file di testo e contare le occorrenze di ogni parola (case-insensitive, ignorando punteggiatura semplice).

# ## Dati forniti
# Un paragrafo hardcoded da scrivere su file:
# ```python
# testo = "Python è un linguaggio di programmazione. Python è semplice e potente."
# ```

# ## Istruzioni

# 1. **Definire `conta_parole(nome_file)`**: Accetta un nome file, legge il contenuto, splitta in parole (ignorando maiuscole e punteggiatura come virgole e punti), e restituisce un dizionario {parola: conteggio}.

# 2. **Definire `stampa_conteggio(dizionario)`**: Accetta il dizionario e lo stampa in ordine alfabetico delle chiavi.

# 3. **Definire `main()`**: 
#    - Definisce `testo` (dati hardcoded)
#    - Scrive `testo` su "esercizio57.txt"
#    - Chiama `conta_parole` e `stampa_conteggio`

# ## Suggerimenti
# - Per scrivere il file iniziale: usa `with open("esercizio57.txt", "w") as f: f.write(testo)`
# - Per contare: converti tutto in lowercase, rimuovi "." e ",", poi `.split()`
# - Usa un dizionario per accumulare conteggi
# - Per ordinare: `sorted(dizionario.items())`

# ## Esempio di output atteso
# ```
# Conteggio parole:
# di: 1
# e: 1
# linguaggio: 1
# potente: 1
# programmazione: 1
# python: 2
# semplice: 1
# un: 1
# è: 2
# ```

def conta_parole(nome_file) -> dict:
    try:
        with open(nome_file, "r" , encoding="utf-8") as file:
            contenuto = file.read()
    except FileNotFoundError:
        print(f"Errore: il file {nome_file}  non è stato trovato.")
    except IOError as e:
        print(f"Errore durante la lettura del file: {e}")  

    contenuto_parole = contenuto.split()
    conteggio = []
    for parola in contenuto_parole:
        conteggio_dopo ={parola : len(parola)}
        conteggio.append(conteggio_dopo) 
    return conteggio   



# Definire stampa_conteggio(dizionario): Accetta il dizionario e lo stampa in ordine alfabetico delle chiavi.

def stampa_conteggio(conteggio) ->None:
    for dict in conteggio:
        print(f"{dict}")



# Definire main():

# Definisce testo (dati hardcoded)
# Scrive testo su "esercizio57.txt"
# Chiama conta_parole e stampa_conteggio




def main():
    testo = "Python è un linguaggio di programmazione. Python è semplice e potente."
    try:
        with open("esercizio57.txt", "w", encoding="utf-8") as file:
            file.write(testo)
    except IOError as e:
        print(f"Errore durante la scrittura del file: {e}")  
    conteggio = conta_parole("esercizio57.txt")
    stampa_conteggio(conteggio)
main()