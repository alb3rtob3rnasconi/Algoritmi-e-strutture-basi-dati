# Programma per calcolare i nodi di un albero K-ario completo
# Basato sulla Serie Geometrica Troncata: N_max = (K^(h+1) - 1) / (K - 1)

def calcola_nodi(k, h):
    """Calcola il numero massimo di nodi in un albero k-ario di altezza h."""
    if k < 2:
        return "Il grado K deve essere almeno 2."
    
    # Calcolo del numeratore: K^(h+1) - 1
    numeratore = (k ** (h + 1)) - 1
    # Calcolo del denominatore: K - 1
    denominatore = k - 1
    
    # Divisione intera
    n_max = numeratore // denominatore
    return n_max

def avvia_programma():
    print("="*50)
    print(" SIMULATORE ALBERI K-ARI (Massimizzazione Nodi) ")
    print("="*50)
    print("Premi Ctrl+C per uscire in qualsiasi momento.\n")
    
    while True:
        try:
            # Richiede i parametri all'utente
            grado_k = int(input("Inserisci il grado dell'albero (K) [es. 2 per Binario]: "))
            altezza_h = int(input("Inserisci l'altezza dell'albero (h): "))
            
            # Esegue il calcolo matematico
            risultato = calcola_nodi(grado_k, altezza_h)
            
            # Mostra la scomposizione della formula per fini didattici
            print("\n--- RISULTATI ---")
            print(f"Formula applicata : ({grado_k}^{altezza_h+1} - 1) / ({grado_k} - 1)")
            print(f"Sviluppo numerico : ({(grado_k**(altezza_h+1))} - 1) / {grado_k-1}")
            print(f"NODI TOTALI (N)   : {risultato}")
            print("-" * 50 + "\n")
            
        except ValueError:
            print("\n[!] Errore: Per favore, inserisci solo numeri interi validi.\n")

# Avvia il ciclo interattivo
if __name__ == "__main__":
    avvia_programma()