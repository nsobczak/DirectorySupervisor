########
# TP1 #
########

# ____________________________________________________________________________________________________
# Config

# Import
import logging
import sys
import argparse


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

def initLog():
    # log format
    # logging.basicConfig(datefmt='', format='%asctime', level=logging.INFO)
    logging.basicConfig(filename='DirectorySupervisor.log',
                        datefmt="%d/%m/%Y-%H:%M:%S", \
                        format="%(asctime)s %(levelname)s %(funcName)s %(message)s", \
                        level=logging.INFO)
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
    # affichage des arguments rentres
    logging.info(
        ":\npath to the directory : %s \npath where to generate log : %s \ndepth of the directory : %s \nfrequency : %s hz\n",
        dp, lp, depth, frequence)


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
    initLog()
    logging.info("Parametres entres : sys.argv = %s", sys.argv)
    initVariablesGlobales()
    # loop()


if __name__ == "__main__":
    monMain()
