#!/usr/bin/python
# -*- coding: utf-8 -*-

#Import nécessaire pour utiliser les fonctions de cette fonction
from constantes.constantes import constanteStructure as const
import generationFormatHtml as genHtml
import generationFormatCsv as genCsv
import time

################ Génération du récapitulatif au format demandé ################
# en paramètre : l'objet qui contient tous les serveurs avec leurs commandes associées et analysées
def funcGenerationRecapitulatif(tabRecapFinal,timeNow,formatFichier):
	
	#on met le format du fichier en minuscule
	formatFichier = formatFichier.lower()
	
	#Analyse du format de fichier demandé
	if formatFichier != "html" and formatFichier != "csv":
		print "ERROR - format demande : INCONNU"
		print "Arret de la generation du recapitulatif."
		exit()
	
	#On boucle sur chaque élément du scénario
	for index, tabRecap in enumerate(tabRecapFinal):
		################ Construction du tableau recapitulatif ################
		#tri du tableau recap par hostname
		tabRecapFinal[index].sort(key=lambda x: x["hostnameServeur"])
		#tri du tableau recap par groupe
		tabRecapFinal[index].sort(key=lambda x: x["groupeServeur"])
		
	######## GENERATION DES FICHIER SELON LE FORMAT DEMANDE
	if formatFichier == "html":
		genHtml.funcGenerationFormatHtml(timeNow,tabRecapFinal)
	elif formatFichier == "csv":
		genCsv.funcGenerationFormatCsv(timeNow,tabRecapFinal)