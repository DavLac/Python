#!/usr/bin/python
# -*- coding: utf-8 -*-

#Import nécessaires pour le fonctionnement du programme
from recuperationListeServeurEtCommande import recuperationCsv as recCsv
from recuperationListeServeurEtCommande import filtrageListeConfigCsv as filListConf
from analyseEtExecutionCommandesSsh import sshExecutionCommandes as sshExec
from generationLogRecapitulatif import generationRecapitulatif as genRecap
import recuperationArgumentCommandeRundeck as recupArg
import time

#Récuperation des arguments de la ligne de commande de RUNDECK
arguments = recupArg.funcRecuperationArgumentCommandeRundeck() #fonction dans le fichier recuperationArgumentCommandeRundeck.py

#Message d'introduction
print "DEBUT PROGRAMME AUDIT"
print ""

#### Récupération de la date au début du script
#La date sera indiquée dans le fichier recapitulatif
#La date/heure est au format "2018-01-30_12-50-22"
timeNow = time.strftime("%Y-%m-%d_%H-%M-%S")

################ RECUPERATION DES CSV ################
#listeConfigCsv comprend la liste des SCENARIOS, la liste des SERVEURS la liste des COMMANDES et la liste des GROUPES DE COMMANDES
listeConfigCsv = recCsv.funcRecuperationCsv(arguments['libelleScenario'])

#Tableau recapitulatif qui contiendra tous les autres tableau recap (resultat des commandes, détail des serveurs...)
tabRecapFinal = []

#Parcours des scenarios et execution des commandes
for scenario in listeConfigCsv['listeScenario']:

	################ Recuperation des elements nécessaires pour ce scénario ################
	filtreListeConfigCsv = filListConf.funcFiltrageListeConfigCsv(listeConfigCsv['listeServeur'],listeConfigCsv['listeGroupeCommandes'],listeConfigCsv['listeCommandes'],scenario)

	################ Connexion SSH sur chacun des serveurs ################
	#initialisation du tableau qui recevra la liste des commandes
	tabRecap = []
	#Fonction qui exécute les commandes en fonction des groupes des serveurs
	tabRecap = sshExec.funcSshExecutionCommandes(filtreListeConfigCsv['listeServeurFiltre'],filtreListeConfigCsv['listeCommandesFiltre'],arguments['commandeType'],scenario) #fichier sshExecutionCommandes.py
	
	#Remplissage du tableau final contenant tous les élements du scenario
	tabRecapFinal.append(tabRecap)

################ Construction du tableau recapitulatif en format HTML ou CSV ################
genRecap.funcGenerationRecapitulatif(tabRecapFinal,timeNow,"html") #fichier generationRecapitulatif.py
genRecap.funcGenerationRecapitulatif(tabRecapFinal,timeNow,"csv") #fichier generationRecapitulatif.py

#Message de fin de programme
print ""
print "FIN PROGRAMME AUDIT"