import os

########################################################################

def Elenco_Doc_Classe(classe, orario_docenti):
    '''
    Funzione che ritorna la lista di docenti di una determinata classe
    
    PARAMETRI:
        -classe: la classe di cui dobbiamo trovare i docenti
        -orario_docenti: la matrice contenente gli orari dei professori
        
    RITORNA:
        -doc: la lista dei docenti della classe
    '''
    
    #Creo la lista per la memorizzazione dei professori
    doc=[]
    
    #Ciclo per la scansione di tutti gli orari
    for i in range(len(orario_docenti)):
        
        #controllo per vedere se la classe che cerchiamo è dentro all'orario del professore
        if (classe) in orario_docenti[i]:
            
            #se la classe è contenuta nell'orario, aggiungo il nome del professore alla lista
            doc.append(orario_docenti[i][0])
    
    return (doc)

########################################################################

def Orario_Docente(docenti,nomedocente):
    '''
    Funzione che ritorna l'orario di un docente chiesto dall'utente e le sue ore in cui lavora
    
    PARAMETRI:
        -docenti: la matrice contenente gli orari dei professori
        -nomedocente: nome del docente di cui si vuole sapere l'orario
    
    RTIORNA:
        -orario: l'orario del professore di cui si vogliono sapere le ore
        -cont: numero di ore del professore
    '''
    
    #Creo una lista nella quale salvare l'orario del professore desiderato
    orario=[]
    
    #Ciclo per scansionare tutte le righe del file
    for i in range(len(docenti)):
        
        #Condizione per controllare se la riga attuale contiene il nome del docente desiderato
        if nomedocente in docenti[i]:
            
            #Ciclo per salvare solo l'orario del professore senza il nome
            for j in range(1,len(docenti[i])):
                orario.append(docenti[i][j])
    
    #Inizializzo la variabile cont a int "0", questa variabile servirà per contare le ore di lavoro di un professore
    cont=0
    
    #Ciclo per scansionare ora per ora l'orario del professore
    for i in range(len(orario)):
        
        #Condizione per controllare se l'ora corrente sia buca o meno
        if orario[i]!="   ":
            #Se l'ora non è vuota allora il contatore di ore di lavoro sale di uno
            cont+=1
    
    return (orario,cont)

########################################################################

def Ore_Disponibili(docenti,nomedocente):
    '''
    Funzione che ritorna il numero di ore disponibili di un professore
    
    PARAMETRI:
        -docenti: la matrice contenente gli orari dei professori
        -nomedocente: nome del docente di cui si vuole sapere l'orario
    
    RITORNA:
        -cont: numero di ore disponibili (D) del docente indicato
    '''
    
    #Creo una lista nella quale salvare l'orario del professore desiderato
    orario=[]
    
    #Ciclo per scansionare tutte le righe del file
    for i in range(len(docenti)):
        
        #Condizione per controllare se la riga attuale contiene il nome del docente desiderato
        if nomedocente in docenti[i]:
            
            #Ciclo per salvare solo l'orario del professore senza il nome
            for j in range(1,len(docenti[i])):
                orario.append(docenti[i][j])
    
    #Inizializzo la variabile cont a int "0", questa variabile servirà per contare le ore di lavoro di un professore
    cont=0
    
    #Ciclo per scansionare ora per ora l'orario del professore
    for i in range(len(orario)):
        
        #Condizione per controllare se l'ora corrente sia disponibile o meno
        if orario[i] == " D ":
            
            #Se l'ora è disponibile allora il contatore di ore di lavoro sale di uno
            cont+=1
    
    return (cont)

########################################################################

def Docente_Ora_Specifica(docenti ,giorno, ora):
    '''
    Funzione per ottenere una lista contenente tutti i nomi dei docenti che hanno lezione un determinato giorno ad una determiata ora
    
    PARAMETRI:
        -docenti: la matrice contenente gli orari dei professori
        -giorno: giorno selezionato dall'utente, formato dalle prime tre lettere in maiuscolo
        -ora: ora selezionata dall'utente, formata da una variabile di tipo intero
    
    RITORNA:
        -ListaDocenti: una lista contenente i nomi di tutti i docenti che hanno lezione il giorno e l'ora specificati dall'utente
    '''
    
    #Creo una lista per salvare i docenti che hanno lezione il giorno e l'ora richiesta dall'utente
    ListaDocenti=[]
    
    #Prima variabile per calcolare dove dovrò puntare dopo
    p1=0
    
    #Condizione per capire quale giorno è stato selezionato e per modificare il puntatore
    if giorno=="LUN":
        p1=0
    elif giorno=="MAR":
        p1=7
    elif giorno=="MER":
        p1=7*2
    elif giorno=="GIO":
        p1=7*3
    elif giorno=="VEN":
        p1=7*4
    
    #definisco il puntatore finale, in base al giorno e all'ora    
    punt = p1 + ora
    
    #Scansiono l'orario di ogni professore
    for i in docenti:
        #Condizione per capire se siamo all'ultima linea o meno
        if len(i)>1:
            #Condizione per capire se il professore ha un'ora di lezione nel giorno e all'ora richiesti dall'utente
            if (i[punt]!="R" and i[punt]!="   "):
                #Se il professore ha lezione allora aggiungo il nome del docente alla lista
                ListaDocenti.append(i[0])
    
    return(ListaDocenti)

########################################################################

def Docenti(righe):
    '''
    Funzione che crea una matrice in cui le liste contenute sono gli orari di ogni professore con all'inizio il nome del professore
    
    PARAMETRI:
        -righe: una lista contenente le righe del file "TabellaGlobale.csv" 
    
    RITORNA:
        -docente: la matrice contenente le liste formate dagli orari di ogni professore
    '''
    
    #Mi creo una matrice per memorizzare le liste di orari 
    docente=[]
    
    #Ciclo per creare e aggiungere alla matrice, le liste contententi gli orari dei professori
    for i in range(2, len(righe)):
        docente.append(righe[i].split(","))
    
    return (docente)

########################################################################

def Lettura_Righe(file):
    '''
    Funzione per la lettura delle righe del file
    
    PARAMETRI:
        -file: il file aperto come stringa unica
        
    RITORNA:
        -righe: una lista contente tutte le righe
    '''
    
    #Creazione della lista Righe nella quale saranno contenute le linee del file letto
    righe=[]
    
    #Leggo la prima riga
    riga=file.readline()
    
    #Aggiungo le righe alla lista
    righe.append(riga)
    while riga:
        riga=file.readline().strip("\n")
        righe.append(riga)
    
    return (righe)

########################################################################