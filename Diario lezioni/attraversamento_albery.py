# Programma per simulare le visite di un Albero Binario
# (Preorder, Inorder, Postorder)

class Nodo:
    def __init__(self, valore):
        self.valore = valore
        self.sinistro = None
        self.destro = None

# --- FUNZIONI DI ATTRAVERSAMENTO RICORSIVE ---

def visita_preorder(nodo, risultato):
    if nodo:
        risultato.append(nodo.valore)               # 1. Visita Radice
        visita_preorder(nodo.sinistro, risultato)   # 2. Esplora Sinistra
        visita_preorder(nodo.destro, risultato)     # 3. Esplora Destra

def visita_inorder(nodo, risultato):
    if nodo:
        visita_inorder(nodo.sinistro, risultato)    # 1. Esplora Sinistra
        risultato.append(nodo.valore)               # 2. Visita Radice
        visita_inorder(nodo.destro, risultato)      # 3. Esplora Destra

def visita_postorder(nodo, risultato):
    if nodo:
        visita_postorder(nodo.sinistro, risultato)  # 1. Esplora Sinistra
        visita_postorder(nodo.destro, risultato)    # 2. Esplora Destra
        risultato.append(nodo.valore)               # 3. Visita Radice

# --- COSTRUZIONE ALBERO ED ESECUZIONE ---

def costruisci_albero():
    # Creiamo l'albero: Radice A; figli B, C; nipoti D, E (sotto B) e F, G (sotto C)
    radice = Nodo('A')
    radice.sinistro = Nodo('B')
    radice.destro = Nodo('C')
    radice.sinistro.sinistro = Nodo('D')
    radice.sinistro.destro = Nodo('E')
    radice.destro.sinistro = Nodo('F')
    radice.destro.destro = Nodo('G')
    return radice

def avvia_programma():
    albero = costruisci_albero()
    
    print("="*50)
    print(" SIMULATORE ATTRAVERSAMENTO ALBERI BINARI ")
    print("="*50)
    print("Struttura dell'albero di test:")
    print("         A         ")
    print("       /   \\       ")
    print("      B     C      ")
    print("     / \\   / \\     ")
    print("    D   E F   G    \n")
    
    while True:
        print("Scegli il tipo di visita:")
        print("1. Preorder  (Radice, Sinistra, Destra)")
        print("2. Inorder   (Sinistra, Radice, Destra)")
        print("3. Postorder (Sinistra, Destra, Radice)")
        print("4. Esci")
        
        scelta = input("\nInserisci la tua scelta (1-4): ")
        risultato = []
        
        if scelta == '1':
            visita_preorder(albero, risultato)
            print(f"\n[!] Risultato PREORDER : {' -> '.join(risultato)}\n")
        elif scelta == '2':
            visita_inorder(albero, risultato)
            print(f"\n[!] Risultato INORDER  : {' -> '.join(risultato)}\n")
        elif scelta == '3':
            visita_postorder(albero, risultato)
            print(f"\n[!] Risultato POSTORDER: {' -> '.join(risultato)}\n")
        elif scelta == '4':
            print("Chiusura programma...")
            break
        else:
            print("\nErrore: Scelta non valida.\n")
        print("-" * 50)

if __name__ == "__main__":
    avvia_programma()