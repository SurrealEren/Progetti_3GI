"Import dei moduli"
from Funzioni import Funzioniinput
from Funzioni import FunzioniMain as f
import os

def menù():
    scelta=Funzioniinput.inputintlim("Funzioni disponibili:\n   1)Lista dei docenti data una classe\n   2)L'orario di un docente e le sue ore totali\n  3)Cognome e nome di un docente dato un numero di ore disponibili\n  4)Elenco dei docenti data una certa ora o un certo giorno\nInserire il numero della funzione che si vuole eseguire: ",0,5)
    return (scelta)

########################################################################

def main():
    "Apro il file in modalità lettura"
    file_lettura=open("OrarioTabellaGlobale.csv", "r")
    
    "Chiamo la funzione per dividere il file in righe"
    righe_file=f.Lettura_Righe(file_lettura)
    "Chiamo la funzione per avere l'orario di ciascun docente"
    orario_docenti=f.Docenti(righe_file)
    
    scelta=menù()
    
    if scelta==1:
        classe=Funzioniinput.inputstr("Inserire la classe di cui si vogliono sapere i docenti: ").upper()
        elenco=f.Elenco_Doc_Classe(classe, orario_docenti)
        filenuovo=open("Docenti della {}.txt".format(classe), "w")
        
        for i in range(len(elenco)):
            filenuovo.write("-" + elenco[i] + "\n")
    elif scelta==2:
        docente=Funzioniinput.inputstr("Inserire il nome del docente di cui si vuole sapere l'orario: ").upper()
        docente20="{:20}".format(docente)
        orario,ore_buche=f.Orario_Docente(orario_docenti, docente20)
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
    elif scelta==3:
        docente=Funzioniinput.inputstr("Inserire il nome del docente di cui si vuole sapere le ore disponibili: ").upper()
        docente20="{:20}".format(docente)
        disponibilita=f.Ore_Disponibili(orario_docenti, docente20)
        filenuovo=open("Disponibilità di {}.txt".format(docente), "w")
        filenuovo.write("Le ore disponibili di {0}, sono: {1}".format(docente, disponibilita))
    elif scelta==4:
        giorno=Funzioniinput.inputstr("Inserire le prime tre lettere del giorno: ").upper()
        ora=Funzioniinput.inputint("Inserire l'ora come numero: ")
        ListaDocenti=f.Docente_Ora_Specifica(orario_docenti, giorno, ora)
        filenuovo=open("Lista dei docenti.txt", "w")
        filenuovo.write("Lista dei docenti disponibili il {0} alla {1}° ora:\n".format(giorno,ora))
        for i in ListaDocenti:
            filenuovo.write("   -" + i + "\n")
    return

########################################################################

main()