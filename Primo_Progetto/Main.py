"Import dei moduli"
from Funzioni import Funzioniinput
from Funzioni import FunzioniMain as f
import os

def menù():
    scelta=Funzioniinput.inputintlim("Funzioni disponibili:\n   1)Lista dei docenti data una classe\n   2)L'orario di un docente e le sue ore totali\n  3)Cognome e nome di un docente dato un numero di ore disponibili\n  4)Elenco dei docenti data una certa ora o un certo giorno\nInserire il numero della funzione che si vuole eseguire: ",0,5)
    return (scelta)

########################################################################

def main():
    #Apro il file in modalità lettura
    file_lettura=open("OrarioTabellaGlobale.csv", "r")
    
    #Chiamo la funzione per dividere il file in righe
    righe_file=f.Lettura_Righe(file_lettura)
    #Chiamo la funzione per avere l'orario di ciascun docente
    orario_docenti=f.Docenti(righe_file)
    
    #Creo una variabile per la ripetizione del programma
    rip="S"
    
    while rip=="S":        
        #Chiamo la funzione per generare il menù di scelta, e per acquisire il numero della funzione da eseguire
        scelta=menù()
        
        #Funzione per la formattazione delle righe stampate sulla shell, stampa righe vuote
        Funzioniinput.spazivuoti(2)
        
        #Cascata di condizioni per eseguire la funzione scelta dall'utente
        if scelta==1:
            #Chiedo all'utente un'input di tipo stringa per la variabile classe
            classe=Funzioniinput.inputstr("Inserire la classe di cui si vogliono sapere i docenti: ").upper()
            
            #chiamo la funzione per ottenere i professori della classe chiesta dall'utente, passando come parametri, la classe e la matrice contenente gli orari di ogni docente
            elenco=f.Elenco_Doc_Classe(classe, orario_docenti)
            
            #Creo il nuovo file in cui mettere il risultato dell'operazione
            filenuovo=open("Docenti della {}.txt".format(classe), "w")
        
            #Ciclo per immetere nel file appena creato i nomi dei professori della classe chiesta
            for i in range(len(elenco)):
                filenuovo.write("   -" + elenco[i] + "\n")
            
            #Mando un messaggio di conferma di creazione del file all'utente, con annesso il nome del file
            print("È stato creato nella cartella corrente il documento: \"Docenti della {}.txt\"".format(classe))
        elif scelta==2:
            #Chiedo all'utente un'input di tipo stringa per la variabile docente
            docente=Funzioniinput.inputstr("Inserire il nome del docente di cui si vuole sapere l'orario: ").upper()
            #Formatto l'input dell'utente per fare in modo che corrisponda alla lunghezza dei nomi riportati sulla tabella
            docente20="{:20}".format(docente)
            
            #Chiamo la funzione per ottenere l'orario e le ore buche di un professore, passando come parametri la matrice contenente gli orari di ogni docente e il nome del docente
            orario,ore_buche=f.Orario_Docente(orario_docenti, docente20)
            
            #Creo il nuovo file in cui mettere il risultato dell'operazione
            filenuovo=open("Orario di {}.txt".format(docente), "w")
            
            #Immetto nel file appena creato le prime due righe d'intestazione
            primerighe=righe_file[0] + righe_file[1]
            filenuovo.write(primerighe)
            
            #Scrivo dentro al file appena creato il nome del docente seguito dal suo orario
            filenuovo.write("\n" + docente20 + ",")
            for i in range(len(orario)):
                if i!=len(orario):
                    filenuovo.write(orario[i] + ",")
                else:
                    filenuovo.write(orario[i])
            
            #Scrivo in fondo al file le ore buche del professore
            filenuovo.write("\nLe numero di ore buche del docente è: " + str(ore_buche))
            
            #Mando un messaggio di conferma di creazione del file all'utente, con annesso il nome del file
            print("È stato creato nella cartella corrente il documento: \"Orario di {}.txt\"".format(docente))
        elif scelta==3:
            #Chiedo all'utente un'input di tipo stringa per la variabile docente
            docente=Funzioniinput.inputstr("Inserire il nome del docente di cui si vuole sapere le ore disponibili: ").upper()
            #Formatto l'input dell'utente per fare in modo che corrisponda alla lunghezza dei nomi riportati sulla tabella
            docente20="{:20}".format(docente)
            
            #Chiamo la funzione per contare le ore disponibili di un determinato professore,passando come parametri la matrice contenente gli orari di ogni docente e il nome del docente
            disponibilita=f.Ore_Disponibili(orario_docenti, docente20)
            
            #Creo il nuovo file in cui mettere il risultato dell'operazione
            filenuovo=open("Disponibilità di {}.txt".format(docente), "w")
            
            #Scrivo dentro al file la linea indicante il numero di ore disponibili di un professore 
            filenuovo.write("Le ore disponibili di {0}, sono: {1}".format(docente, disponibilita))
            
            #Mando un messaggio di conferma di creazione del file all'utente, con annesso il nome del file
            print("È stato creato nella cartella corrente il documento: \"Disponibilità di {}.txt\"".format(docente))
        elif scelta==4:
            #Chiedo all'utente un'input di tipo stringa per la variabile giorno
            giorno=Funzioniinput.inputstr("Inserire le prime tre lettere del giorno: ").upper()
            
            #Chiedo all'utente un'input di tipo intero per la variabile ora 
            ora=Funzioniinput.inputint("Inserire l'ora come numero: ")
            
            #Chiamo la funzione per per ottenere i professori che hanno lezione un giorno specifico ad un'ora specifica, passando come parametri la matrice contenente gli orari di ogni docente, il giorno, e l'ora
            ListaDocenti=f.Docente_Ora_Specifica(orario_docenti, giorno, ora)
            
            #Creo il nuovo file in cui mettere il risultato dell'operazione
            filenuovo=open("Lista dei docenti.txt", "w")
            
            #Scrivo nel documento appena creato la lista dei docenti formattata tramite un ciclo
            filenuovo.write("Lista dei docenti disponibili il {0} alla {1}° ora:\n".format(giorno,ora))
            for i in ListaDocenti:
                filenuovo.write("   -" + i + "\n")
                
            #Mando un messaggio di conferma di creazione del file all'utente, con annesso il nome del file
            print("È stato creato nella cartella corrente il documento: \"Lista dei docenti.txt\"")

        #Modifico il valore di "rip" per entrare dentro al ciclo di richiesta dell'input per la ripetzione del programma
        rip=""
        
        #Stampo due righe vuote per la formattazione
        Funzioniinput.spazivuoti(2)
        #Chiedo un'input di tipo stringa all'utente per ripetere il programma
        while (rip!="S" or rip!="N"):
            rip=Funzioniinput.inputstr("Vuoi usare un'altra funzione?\nSì[S]    No[N]").upper
        #Stampo due righe vuote per la formattazione
        Funzioniinput.spazivuoti(2)
            
        
    #Stampo un messagio per segnalare la chiusura del programma
    print("Grazie per aver usato questo programma.\nScritto da: Perera Eshan Sandika Limal")
    return

########################################################################

main()