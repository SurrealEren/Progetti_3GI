#Funzioni Utili
def spazivuoti(n):
    '''
    Funzione che stampa n righe vuote
    
    PARAMETRI:
        -n: numero di righe vuote da stampare
    '''
    for i in range(n):    #Ciclo per stampare le righe vuote
        print("")
    return

def inputint(a):
    '''
    Funzione che controlla l'input dell'utente per fare in modo che sia di tipo intero, con messaggio d'errore
    
    PARAMETRI:
        -a: Stringa per la richiesta dell'input
        
    RITORNI:
        -x: input di tipo INT ddell'utente
    '''
    try:    #Prova a chiedere l'input all'utente
        x=int(input(a))    #Durante l'input impone che il valore sia di tipo intero
    except ValueError:     #Se l'input inserito dall'utente non è di tipo intero, quindi in caso di ValueError, manda il messaggio d'errore
        spazivuoti(1)
        x=inputint("ERRORE ERRORE ERRORE!!!\nInserire un valore Intero: ")    #Richiama la funzione inputint mandano come parametro il messaggio d'errore
    return(x)

def inputreali(a):
    '''
    Funzione che controlla l'input dell'utente per fare in modo che sia di tipo reale, con messaggio d'errore
    
    PARAMETRI:
        -a: Stringa per la richiesta dell'input
        
    RITORNI:
        -x: input di tipo INT ddell'utente
    '''
    try:    #Prova a chiedere l'input all'utente
        x=float(input(a))    #Durante l'input impone che il valore sia di tipo reale
    except ValueError:       #Se l'input inserito dall'utente non è di tipo reale, quindi in caso di ValueError, manda il messaggio d'errore
        spazivuoti(1)
        x=inputint("ERRORE ERRORE ERRORE!!!\nInserire un valore Reale: ")    #Richiama la funzione inputreali mandano come parametro il messaggio d'errore
    return(x)

def inputstr(a):
    '''
    Funzione che controlla l'input dell'utente per fare in modo che sia di tipo stringa, con messaggio d'errore
    
    PARAMETRI:
        -a: Stringa per la richiesta dell'input
        
    RITORNI:
        -x: input di tipo INT ddell'utente
    '''
    try:    #Prova a chiedere l'input all'utente
        x=str(input(a))    #Durante l'input impone che il valore sia di tipo stringa
    except ValueError:     #Se l'input inserito dall'utente non è di tipo stringa, quindi in caso di ValueError, manda il messaggio d'errore
        spazivuoti(1)
        x=inputint("ERRORE ERRORE ERRORE!!!\nInserire un valore Stringa: ")    #Richiama la funzione inputstr mandano come parametro il messaggio d'errore
    return(x)

def inputbool(a):
    '''
    Funzione che controlla l'input dell'utente per fare in modo che sia di tipo Booleano, con messaggio d'errore
    
    PARAMETRI:
        -a: stringa di richesta dell'input
    
    RITORNI:
        -x: valore Booleano che può essere "True" o "False"
    '''
    b=inputstr.lower(a)    #Chiede un'input di tipo stringa all'utente, e lo rende minuscolo
    if (b=="true"):        #Se l'input dato è "True"
        x=True
    elif (b=="false"):     #Se l'input dato è "False"
        x=False
    else:                  #Se nessuno dei due manda un messaggio d'errore e richiede l'input
        spazivuoti(1)
        x=inputbool("ERRORE ERRORE ERRORE!!!\nInserire un valore di tipo Booleano: ")
    return(x)

def inputintlim(a,l1,l2):
    ''''
    Funzione che chiede un'input di tipo "int", il quale deve essere compreso tra due numeri dati dall'utente, limiti esclusi
    
    PARAMETRI:
        -a: stringa di richiesta dell'input
        -l1: primo limite dell'input (minore)
        -l2: secondo limite dell'input (maggiore)
        
    RITORNA:
        -x: valore "int" valido inserito dall'utente
    '''
    x=inputint(a)    #chiede un'input di tipo "int" all'utente
    while (x<=l1) or (x>=l2):    #Continua a richiedere l'input all'utente finchè non è compreso tra i due limiti, mandando sempre il messaggio d'errore
        x=inputint("ERRORE ERRORE ERRORE!!!\nInserire un valore compreso tra {0} e {1}".format(l1,l2))
    return(x)

def inputrealilim(a,l1,l2):
    ''''
    Funzione che chiede un'input di tipo "float", il quale deve essere compreso tra due numeri dati dall'utente, limiti esclusi
    
    PARAMETRI:
        -a: stringa di richiesta dell'input
        -l1: primo limite dell'input (minore)
        -l2: secondo limite dell'input (maggiore)
        
    RITORNA:
        -x: valore "int" valido inserito dall'utente
    '''
    x=inputint(a)    #chiede un'input di tipo "float" all'utente
    while (x<=l1) or (x>=l2):    #Continua a richiedere l'input all'utente finchè non è compreso tra i due limiti, mandando sempre il messaggio d'errore
        x=inputreali("ERRORE ERRORE ERRORE!!!\nInserire un valore compreso tra {0} e {1}".format(l1,l2))
    return(x)

def lista(a):
    x=input(a).strip().split()
    return x

def inputintpos(a,l1):
    ''''
    Funzione che chiede un'input di tipo "int", il quale deve essere maggiore di un valore dato alla funzione (limite escluso)
    
    PARAMETRI:
        -a: stringa di richiesta dell'input
        -l1: valore minimo dell'input
        
    RITORNA:
        -x: valore "int" valido inserito dall'utente
    '''
    x=inputint(a)    #chiede un'input di tipo "int" all'utente
    while (x<l1):    #Continua a richiedere l'input all'utente finchè non è maggiore del valore dato, mandando sempre il messaggio d'errore
        x=inputint("ERRORE ERRORE ERRORE!!!\nInserire un valore maggiore di {0}".format(l1))
    return(x)

def inputrealipos(a,l1):
    x=inputint(a)    #chiede un'input di tipo "float" all'utente
    while (x<l1):    #Continua a richiedere l'input all'utente finchè non è maggiore del valore dato, mandando sempre il messaggio d'errore
        x=inputreali("ERRORE ERRORE ERRORE!!!\nInserire un valore maggiore di {0}".format(l1))
    return(x)