# # Esercizio 59: Gestione Inventario Prodotti

# ## Obiettivo
# Gestire un inventario di prodotti in formato JSON, con funzioni per filtrare per categoria e calcolare il valore totale.

# ## Dati forniti
# Una lista di prodotti hardcoded:
# ```python
# prodotti = [
#     {"nome": "Mela", "categoria": "Frutta", "prezzo": 2.5, "quantita": 10},
#     {"nome": "Pane", "categoria": "Pane", "prezzo": 1.0, "quantita": 5},
#     {"nome": "Banana", "categoria": "Frutta", "prezzo": 1.8, "quantita": 8}
# ]
# ```

# ## Istruzioni

# 1. **Definire `salva_inventario(prodotti, nome_file)`**: Accetta una lista di dizionari e un nome file. Salva la lista in JSON con indentazione.

# 2. **Definire `carica_inventario(nome_file)`**: Accetta un nome file e restituisce la lista di dizionari caricata da JSON.

# 3. **Definire `filtra_per_categoria(prodotti, categoria)`**: Accetta la lista prodotti e una stringa categoria. Restituisce una lista con i prodotti di quella categoria.

# 4. **Definire `calcola_totale_categoria(prodotti, categoria)`**: Accetta la lista prodotti e una categoria. Calcola e restituisce il valore totale (prezzo * quantita) per i prodotti di quella categoria.

# 5. **Definire `main()`**: 
#    - Definisce `prodotti` (dati hardcoded)
#    - Chiama `salva_inventario` su "inventario.json"
#    - Chiama `carica_inventario` per ottenere i dati
#    - Filtra per "Frutta" e calcola il totale
#    - Stampa i prodotti filtrati e il totale

# ## Suggerimenti
# - Importa `json`
# - Usa `json.dump` e `json.load` come negli esercizi precedenti
# - Per filtrare: usa un ciclo for e append se categoria corrisponde
# - Per totale: somma prezzo*quantita solo per prodotti filtrati
# - Gestisci errori di file (FileNotFoundError)

# ## Esempio di output atteso
# ```
# File 'inventario.json' salvato con successo.
# Prodotti Frutta: [{'nome': 'Mela', 'categoria': 'Frutta', 'prezzo': 2.5, 'quantita': 10}, {'nome': 'Banana', 'categoria': 'Frutta', 'prezzo': 1.8, 'quantita': 8}]
# Totale valore Frutta: 39.4
# ```



# 1. **Definire `salva_inventario(prodotti, nome_file)`**: Accetta una lista di dizionari e un nome file. Salva la lista in JSON con indentazione.

# 2. **Definire `carica_inventario(nome_file)`**: Accetta un nome file e restituisce la lista di dizionari caricata da JSON.


import json
def salva_inventario(prodotti,nome_file) -> None:
    try:
        with open(nome_file,"w",encoding="utf-8") as f:
            json.dump(prodotti,f,indent=4)
        print(f"\nFile {nome_file} creato con successo.")
    except IOError as e:
        print(f"Errore di scrittura con JSON:  {e}")


def carica_inventario(nome_file) -> list:
    inventario =[]
    try:
        with open(nome_file,"r",encoding="utf-8") as f:
            prodotti_letti = json.load(f)
    except IOError as e:
        print(f"Errore di lettura in JSON: {e}")
    inventario.append(prodotti_letti)
    return inventario

# 3. **Definire `filtra_per_categoria(prodotti, categoria)`**: Accetta la lista prodotti e una stringa categoria. Restituisce una lista con i prodotti di quella categoria.

# 4. **Definire `calcola_totale_categoria(prodotti, categoria)`**: Accetta la lista prodotti e una categoria. Calcola e restituisce il valore totale (prezzo * quantita) per i prodotti di quella categoria.




def filtra_per_categoria(prodotti,categoria) -> list:
    filtrata = []
    for prodotto in prodotti:
        if prodotto["categoria"] == categoria:
            filtrata.append(prodotto["nome"])
    return filtrata


def calcola_totale_categoria(prodotti,categoria) ->float:
    for prodotto in prodotti:
        if prodotto["categoria"] == categoria:
            prezzo_tot = prodotto["prezzo"] * prodotto["quantita"]
    return prezzo_tot
            


# 5. **Definire `main()`**: 
#    - Definisce `prodotti` (dati hardcoded)
#    - Chiama `salva_inventario` su "inventario.json"
#    - Chiama `carica_inventario` per ottenere i dati
#    - Filtra per "Frutta" e calcola il totale
#    - Stampa i prodotti filtrati e il totale


def main() -> None:
    prodotti = [
    {"nome": "Mela", "categoria": "Frutta", "prezzo": 2.5, "quantita": 10},
    {"nome": "Pane", "categoria": "Pane", "prezzo": 1.0, "quantita": 5},
    {"nome": "Banana", "categoria": "Frutta", "prezzo": 1.8, "quantita": 8}
]
    salva_inventario(prodotti,"prodotti.json")
    lettura = carica_inventario("prodotti.json")
    categoria = input("Inserisci una categoria: ")
    filtra = filtra_per_categoria(prodotti,categoria)
    totale = calcola_totale_categoria(prodotti,categoria)
    print(f"Dati letti:\n{lettura}")
    print(f"Prodotti filtrati per {categoria}: {filtra}")
    print(f"Valore totale per {categoria}: {totale}")

if __name__ == "__main__":
    main()

            