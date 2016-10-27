# DirectorySupervisor

## What is DirectorySupervisor ?
DirectorySupervisor is a commandline program that generate log files to supervise the activity of a directory.

but = superviser un dossier

- ajout/supppression de fichiers/dossiers
- faire des fichier log : ajout/suppression/modification

## parametres

|Nom du paramètre|commande du paramètre|
|---|---|
|nom du dossier|-dp (directory path)|
|fréquence de supervision|-f|
|chemin du fichier de log|-lp (log path)|
|profondeur de recherche (y'a des dossiers dans les dossiers)|-d (depth)|

on ne sait pas ce qu'il y a dans les dossiers

en lignes de commande => sys.argv

## imposé

- module logging
- module argparse - traitement de parametre 
- module os.path -> pour cross platform
- main

parcourir un dossier => os.walk

## Plan

- determiner une fréquence : entre 1 et 2 hz 
- ne générer des logs que si modifications
- prendre une "image" de l'arbre du dossier, puis comparer à la fréquence donnée => idée = liste

format : jour de la semaine, n°jour mois année HH:MM:SS

### liste de fonctions

- dateDerniereModif(String fichier) : date

#### Var globale

- arbrePrecedent
- frequence
- dp
- lp 
- depth

#### Sys.argv

- splitArgv(String[] Argv) : return [ ["-f", 23], ["-dp", "eherhgig"], ...]
	sépare chaque argument, cf argparse

- analyse1ArgumentArgv(list[]) : maj var globale correspondante
	ex :list = ["-f", 23]

- initVariablesGlobales(String[] Argv) : 
	split
	dp = 
	lp =
	d =
	arbrePrecedent = créeArbre(dp, d)
	frequence = 
	
#### Arbre

- creeArbre(String dp, profondeur) , si arbrePrecedent==null

- compareArbre(String dp)
	nouvelArbre = crée arbre
	compare à l'ancien
	si différent alors log (3 cas) + maj ancien arbre (global)
		idée 3 liste ou 3 fonctions qui sont en-dessous

- estAjoute(arbrePrecedent, arbreActuel)
- estModifie(arbrePrecedent, arbreActuel)
- estSupprime(arbrePrecedent, arbreActuel)

import os.path
	getntime(filename) : date de modif du fichier

#### Arrêt

- stop() : fonction arrêt de la boucle = de la supervision du dossier
regarder à chaque coup de clock si arrêt entrée

#### Log

Voir comment on créer fichier log

Ecrire si y'a ajout, modif, suppression
	forme : type de log(add, mod, suppr), chemin, date

eventuellement une fonction qui évite de réécrire le chemin à chaque fois

## Main

- initVariablesGlobales()

- loop()
	si stop() => arrêt
	sinon
		compareArbre()



- main
	initVariablesGlobales()
	loop()
