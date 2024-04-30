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
    b=input.lower(a)
    if (b=="true"):
        x=True
    elif (b=="false"):
        x=False
    else:
        spazivuoti(1)
        x=inputbool("ERRORE ERRORE ERRORE!!!\nInserire un valore di tipo Booleano: ")
    return(x)

def inputintlim(a,l1,l2):
    x=inputint(a)
    while (x<=l1) or (x>=l2):
        x=inputint("ERRORE ERRORE ERRORE!!!\nInserire un valore compreso tra {0} e {1}".format(l1,l2))
    return(x)

def inputrealilim(a,l1,l2):
    x=inputint(a)
    while (x<=l1) or (x>=l2):
        x=inputreali("ERRORE ERRORE ERRORE!!!\nInserire un valore compreso tra {0} e {1}".format(l1,l2))
    return(x)

def lista(a):
    x=input(a).strip().split()
    return x

def inputintpos(a,l1):
    x=inputint(a)
    while (x<l1):
        x=inputint("ERRORE ERRORE ERRORE!!!\nInserire un valore maggiore di {0}".format(l1))
    return(x)

def inputrealipos(a,l1):
    x=inputint(a)
    while (x<l1):
        x=inputreali("ERRORE ERRORE ERRORE!!!\nInserire un valore maggiore di {0}".format(l1))
    return(x)