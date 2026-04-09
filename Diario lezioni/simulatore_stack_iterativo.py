# Programma per simulare le Visite Iterative (tramite Stack esplicito)
# Focus: Gestione delle ambiguità nel Postorder tramite Flag Booleano

class Nodo:
    def __init__(self, valore):
        self.valore = valore
        self.sinistro = None
        self.destro = None

def costruisci_albero():
    # Albero: Radice A; figli B, C.
    radice = Nodo('A')
    radice.sinistro = Nodo('B')
    radice.destro = Nodo('C')
    return radice

def stampa_stato_stack(azione, stack, estrazione=None):
    """Funzione di supporto per stampare la tabella di tracciamento."""
    stack_str = "Fondo [ " + " | ".join(str(item) for item in stack) + " ] Cima"
    estratto_str = f"Estratto: {estrazione}" if estrazione else ""
    print(f"{azione:<25} {estratto_str:<25} Stack: {stack_str}")

# --- 1. PREORDER ITERATIVO ---
def preorder_iterativo(radice):
    print("\n--- INIZIO PREORDER ITERATIVO (LIFO: Inserisco DX, poi SX) ---")
    if not radice: return
    
    stack = [radice.valore]
    stampa_stato_stack("Stato Iniziale", stack)
    
    while stack:
        corrente = stack.pop()
        stampa_stato_stack("POP (Visito Subito)", stack, corrente)
        
        # Inserisco il figlio destro (andrà a fondo)
        # Inserisco il figlio sinistro (starà in cima)
        # N.B. Per semplicità logica simuliamo i figli hard-coded dell'albero A->B,C
        if corrente == 'A':
            stack.append('C')
            stack.append('B')
            stampa_stato_stack("PUSH figli di A (C, B)", stack)

# --- 2. POSTORDER ITERATIVO (Il trucco del Post-It) ---
def postorder_iterativo(radice):
    print("\n--- INIZIO POSTORDER ITERATIVO (Trucco del Flag/Post-It) ---")
    if not radice: return
    
    # Lo stack contiene tuple: (ValoreNodo, Espandere?)
    # Espandere = True (Da smontare), False (Pronto da stampare)
    stack = [(radice.valore, True)]
    stampa_stato_stack("Stato Iniziale", stack)
    
    while stack:
        corrente, espandere = stack.pop()
        
        if espandere:
            stampa_stato_stack("POP da ESPANDERE", stack, f"{corrente} (TRUE)")
            
            # Ordine di push:
            # 1. Nodo stesso con flag FALSE (Pronto per la visita successiva)
            stack.append((corrente, False))
            
            # Simuliamo l'inserimento dei figli per il nodo A
            if corrente == 'A':
                # 2. Figlio Destro con flag TRUE
                stack.append(('C', True))
                # 3. Figlio Sinistro con flag TRUE
                stack.append(('B', True))
                
            stampa_stato_stack("PUSH completato", stack)
            
        else:
            # Il flag è False: i sottoalberi sono stati esauriti
            stampa_stato_stack("POP PRONTO (Visita!)", stack, f"{corrente} (FALSE)")

# --- MENU DI AVVIO ---
def avvia_programma():
    print("="*60)
    print(" SIMULATORE STACK: VISITE ITERATIVE ")
    print("="*60)
    print("Albero di Test:    A    ")
    print("                  / \\   ")
    print("                 B   C  \n")
    
    preorder_iterativo(costruisci_albero())
    print("\n" + "="*60)
    postorder_iterativo(costruisci_albero())
    print("="*60)

if __name__ == "__main__":
    avvia_programma()