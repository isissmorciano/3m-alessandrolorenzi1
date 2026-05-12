# # Esercizio 58: Gestione di un File JSON con Dati Studenti

# ## Obiettivo
# Salvare e caricare una lista di studenti (dizionari) in formato JSON, calcolando la media dei voti.

# ## Dati forniti
# Una lista di studenti hardcoded:
# ```python
# studenti = [
#     {"nome": "Alice", "voto": 8},
#     {"nome": "Bob", "voto": 7},
#     {"nome": "Carlo", "voto": 9}
# ]
# ```

# ## Istruzioni

# 1. **Definire `salva_studenti(studenti, nome_file)`**: Accetta una lista di dizionari e un nome file. Salva la lista in JSON con indentazione.

# 2. **Definire `carica_studenti(nome_file)`**: Accetta un nome file e restituisce la lista di dizionari caricata da JSON.

# 3. **Definire `calcola_media(studenti)`**: Accetta la lista e restituisce la media dei voti (float).

# 4. **Definire `main()`**: 
#    - Definisce `studenti` (dati hardcoded)
#    - Chiama `salva_studenti` su "studenti.json"
#    - Chiama `carica_studenti` e `calcola_media`
#    - Stampa la lista caricata e la media

# ## Suggerimenti
# - Importa `json`
# - Usa `json.dump` per salvare (con `indent=4`)
# - Usa `json.load` per caricare
# - Gestisci `FileNotFoundError` in caricamento
# - Per media: somma voti / len(studenti)

# ## Esempio di output atteso
# ```
# File 'studenti.json' salvato con successo.
# Studenti caricati: [{'nome': 'Alice', 'voto': 8}, {'nome': 'Bob', 'voto': 7}, {'nome': 'Carlo', 'voto': 9}]
# Media voti: 8.0
# ```

import json

def salva_studenti(studenti,nome_file) ->None:
    try:
        with open(nome_file, "w", encoding="utf-8") as f:
            json.dump(studenti,f,indent=4)
        print(f"\nFile {nome_file} creato con successo.")
    except IOError as e:
        print(f"Errore di scrittura JSON: {e}")
        
    
# 2. **Definire `carica_studenti(nome_file)`**: Accetta un nome file e restituisce la lista di dizionari caricata da JSON.


def carica_studenti(nome_file) -> list:
    lista = []
    try:
        with open(nome_file, "r", encoding="utf-8") as f:
            dati_letti = json.load(f)
    except IOError as e:
        print(f"Errore di lettura in JSON :{e}")
    lista.append(dati_letti)
    return lista
# 3. **Definire `calcola_media(studenti)`**: Accetta la lista e restituisce la media dei voti (float).


def calcola_media(studenti) -> float:
    somma = 0
    for studente in studenti:
        somma = somma + studente["voto"] 
        
    media = somma/len(studenti)
    return media


# 4. **Definire `main()`**: 
#    - Definisce `studenti` (dati hardcoded)
#    - Chiama `salva_studenti` su "studenti.json"
#    - Chiama `carica_studenti` e `calcola_media`
#    - Stampa la lista caricata e la media


            
def main() -> None:
    studenti = [
    {"nome": "Alice", "voto": 8},
    {"nome": "Bob", "voto": 7},
    {"nome": "Carlo", "voto": 9}
    ]
    salva_studenti(studenti, "studenti.json")
    lista = carica_studenti("studenti.json")
    media = calcola_media(studenti)
    print(lista)
    print(f"La media dei voti è {media}")

if __name__ == "__main__":
    main()