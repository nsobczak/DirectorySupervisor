#######
# TP1 #
#######

# TODO : Remplacer print des arbres par des logs + créer fonction loop
# ____________________________________________________________________________________________________
# Config

# Import
import logging
import sys
import argparse
import os
import time

# ____________________________________________________________________________________________________
# ____________________________________________________________________________________________________
# Variables globales

arbrePrecedent = None
frequence = None
depth = None
dp = None
lp = None
logger = None


# ____________________________________________________________________________________________________
# Fonctions d'initialisation

def initLog(logPath):
    """
    log format
    logging.basicConfig(datefmt='', format='%asctime', level=logging.INFO)
    """
    logging.basicConfig(
        filename=logPath + "/DirectorySupervisor.log", \
        datefmt="%d/%m/%Y-%H:%M:%S", \
        format="%(asctime)s %(levelname)s %(funcName)s %(message)s", \
        level=logging.INFO)  # 'filename': '/path/to/DirectorySupervisor.debug.log',
    logging.info("Programme lancé")


def initVariablesGlobales():
    """
    Fonction qui initialise les variables globales en fonction de ce que l'utilisateur a entre.
    La fonction genere une info récapitulant la liste des parametres entres.
    """
    global dp
    global lp
    global depth
    global frequence

    parser = argparse.ArgumentParser(description='Supervision de dossier')
    # obligatoire
    parser.add_argument("dp", type=str, help="path to the directory")
    parser.add_argument("lp", type=str, help="path where to generate log")
    # optionnel
    parser.add_argument("-d", "--depth", default=2, help="depth of the directory")
    parser.add_argument("-f", "--frequence", default=1, help="add frequency in hz")

    # initialisation des parametres globaux
    args = parser.parse_args()
    dp = args.dp
    lp = args.lp
    depth = args.depth
    frequence = args.frequence


def afficheArgument():
    """affichage des arguments rentres"""
    logging.info(
        ":\npath to the directory : %s \npath where to generate log : %s \ndepth of the directory : %s \nfrequency : %s hz\n",
        dp, lp, depth, frequence)


# ___________________________________________________________________________________________________
# Fonctions de creation de l'arbre du dossier et de comparaison

def creatSurveyList(tree):
    """
    create a list of tupples form by (fileName, dateOfLastModif) corresponding to the files in the tree
    """
    listOfModifFiles = []
    i = 0
    while (i < len(tree)):
        path, dirs, files = tree[i]
        level = path.count(os.sep) - startinglevel
        if (level <= depth_max):
            print('### depth ', level, ' ### ', path, ' #####')
            print("Sous dossiers : %s" % dirs)
            print("Fichiers : %s" % files)
            for file in files:
                modifTime = os.path.getmtime(os.path.join(path, file))
                listOfModifFiles += [(file, modifTime)]
        i += 1
    return (listOfModifFiles)


def comparateSurveyList(oldListe, newListe):
    """
	args 2 lists which will be compared
	return 3 lists :
		- for the modified files
		- for the added files
		- for the deleted files
	"""
    if oldListe == newListe:
        return None
    else:
        listOfSupprFiles = []
        listOfAddFiles = []
        listOfModifFiles = []
        isCreated = [True] * len(newListe)
        for o in oldListe:
            isDeleted = True
            for n in newListe:
                nIndex = newListe.index(n)
                oName, oTime = o
                nName, nTime = n
                if oName == nName:
                    isDeleted = False
                    isCreated[nIndex] = False
                    if oTime != nTime:
                        listOfModifFiles += [n]
            if isDeleted:
                listOfSupprFiles += [o]
        for n in newListe:
            nIndex = newListe.index(n)
            if isCreated[nIndex]:
                listOfAddFiles += [n]
        return (listOfModifFiles, listOfAddFiles, listOfSupprFiles)


def logTheMADLists(M, A, D):
    """
    	log the informations contained in the 3 lists :
    		-M = modified files
    		-A = added files
    		-D = deleted files
    """
    if len(M):
        print("M")
        for (mFile, mTime) in M:
            print(time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(mTime)), mFile, " is modified")
    if len(A):
        print("A")
        for (aFile, aTime) in A:
            print(time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(aTime)), aFile, " is added")
    if len(D):
        print("D")
        for (dFile, dTime) in D:
            print(time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(dTime)), dFile, " is deleted")


# ___________________________________________________________________________________________________
# Fonctions principales

def loop():
    """
    si stop() => arret
	sinon
		compareArbre()
    """

    return 1


# ____________________________________________________________________________________________________
# ____________________________________________________________________________________________________
def monMain():
    initVariablesGlobales()
    initLog(lp)
    afficheArgument()
    loop()


if __name__ == "__main__":
    monMain()
