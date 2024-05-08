"Import dei moduli"
from Funzioni import *
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

def menù():
    scelta=Funzioniinput.inputintlim("Funzioni disponibili:\n   1)Lista dei docenti data una classe\n   2)L'orario di un docente e le sue ore totali\n  3)Cognome e nome di un docente dato un numero di ore disponibili\n  4)Elenco dei docenti data una certa ora o un certo giorno\nInserire il numero della funzione che si vuole eseguire: ",0,5)
    return (scelta)

########################################################################

def main():
    "Apro il file in modalità lettura"
    file_lettura=open("OrarioTabellaGlobale.csv", "r")
    
    "Chiamo la funzione per dividere il file in righe"
    righe_file=Lettura_Righe(file_lettura)
    "Chiamo la funzione per avere l'orario di ciascun docente"
    orario_docenti=Docenti(righe_file)
    
    scelta=menù()
    if scelta==1:
        classe=Funzioniinput.inputstr("Inserire la classe di cui si vogliono sapere i docenti: ").upper()
        elenco=Elenco_Doc_Classe(classe, orario_docenti)
        filenuovo=open("Docenti della {}.txt".format(classe), "w")
        for i in range(len(elenco)):
            filenuovo.write("-" + elenco[i] + "\n")
    elif scelta==2:
        docente=Funzioniinput.inputstr("Inserire il nome del docente di cui si vuole sapere l'orario: ").upper()
        docente20="{:20}".format(docente)
        orario,ore_buche=Orario_Docente(orario_docenti, docente20)
        filenuovo=open("Orario di {}.txt".format(docente), "w")
        primerighe=righe_file[0] + righe_file[1]
        filenuovo.write(primerighe)
        filenuovo.write("\n" + docente20 + ",")
        for i in range(len(orario)):
            if i!=len(orario):
                filenuovo.write(orario[i] + ",")
            else:
                filenuovo.write(orario[i])
        filenuovo.write("\nLe numero di ore buche del docente è: " + str(ore_buche))
    return

########################################################################

main()