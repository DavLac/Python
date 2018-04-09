#!/usr/bin/python
# -*- coding: utf-8 -*-

#Import nécessaire pour utiliser les fonctions de cette fonction
import csv
from constantes.constantes import constanteStructure as const

################ Fonction recuperation de la liste des commandes du CSV ################
def funcRecuperationListeCommandes():

	#initialisation du tableau qui recevra la liste des commandes
	listeCommandes = []
	
	print "DEBUT - Recuperation de la liste des commandes du CSV"
	print "Fichier : " + const.cheminFichierListeCommandesCsv
	
	#Cette variable permet de sauter la première ligne du CSV pour ne pas prendre en compte les en-tete
	skipEnteteCsv = False

	try:
		#ouverture du fichier
		with open(const.cheminFichierListeCommandesCsv, 'r') as f:
			reader = csv.reader(f, delimiter=';')
			#la boucle parcours le CSV
			for row in reader:
				#on saute les entêtes du CSV
				if skipEnteteCsv == False:
					skipEnteteCsv = True
					continue
				else:
					#remplissage de la liste 'listeCommandes' en fonction du CSV
					listeCommandes.append({'libelle': row[0],'execution': row[1], 'typeVerification': row[2], 'resultatAttendu' : row[3], 'marge' : row[4], 'groupeCommande' : row[5]})
		
		print "SUCCES - Recuperation de la liste des commandes du CSV"
		print " "
	
	except Exception as e:
		#Exception si probleme de lecture du JSON des commandes
		print "ERROR - Probleme d'ouverture de la liste des commandes (fichier CSV)"
		print "Erreur : " + str(e)
		print "Chemin du fichier : " + const.cheminFichierListeCommandesCsv
		
		#fin du programme
		print ""
		print "ERROR - FIN PROGRAMME AUDIT"
		exit()
	
	else:
		#On retourne la liste des commandes avec leurs détails
		return listeCommandes