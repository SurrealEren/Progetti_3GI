import os

########################################################################

def Docenti(righe):
    docente=[]
    for i in range(2, len(righe)):
        docente.append(righe[i].split(","))
    return (docente)

########################################################################

def Lettura_Righe(file):
    "Creazione della lista Righe nella quale saranno contenute le linee del file letto"
    Righe=[]
    "Leggo la prima riga"
    riga=file.readline()
    "Aggiungo le righe alla lista"
    Righe.append(riga)
    while riga:
        riga=file.readline().strip("\n")
        Righe.append(riga)
    return (Righe)

########################################################################

def Elenco_Doc_Classe(classe, orario_docenti):
    doc=[]
    for i in range(len(orario_docenti)):
        if (classe) in orario_docenti[i]:
            doc.append(orario_docenti[i][0])
    return (doc)

########################################################################

def Orario_Docente(docenti,nomedocente):
    orario=[]
    for i in range(len(docenti)):
        if nomedocente in docenti[i]:
            for j in range(1,len(docenti[i])):
                orario.append(docenti[i][j])
    cont=0
    
    for i in range(len(orario)):
        if orario[i]!="   ":
            cont+=1
    
    return (orario,cont)

########################################################################

def Ore_Disponibili(docenti,nomedocente):
    orario=[]
    
    for i in range(len(docenti)):
        if nomedocente in docenti[i]:
            for j in range(1,len(docenti[i])):
                orario.append(docenti[i][j])
    
    cont=0
    
    for i in range(len(orario)):
        if orario[i] == " D ":
            cont+=1
    
    return (cont)

########################################################################

def Docente_Ora_Specifica(docenti ,giorno, ora):
    ListaDocenti=[]
    "Prima variabile per calcolare dove dovrò puntare dopo"
    p1=0
    
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
        
    punt = p1 + ora
    
    for i in docenti:
        if len(i)>1:
            if (i[punt]!="R" and i[punt]!="   "):
                ListaDocenti.append(i[0])
    
    return(ListaDocenti)