#!/usr/bin/python
# -*- coding: utf-8 -*-

#Import nécessaire pour utiliser les fonctions de cette fonction
import csv
from constantes.constantes import constanteStructure as const

################ Fonction recuperation de la liste des serveurs du CSV ################
def funcRecuperationListeServeurs():

	#initialisation du tableau qui recevra la liste des serveurs
	listeServeur = []
	
	print "DEBUT - Recuperation de la liste des serveurs du CSV"
	print "Fichier : " + const.cheminFichierListeServeurCsv
	
	#Cette variable permet de sauter la première ligne du CSV pour ne pas prendre en compte les en-tete
	skipEnteteCsv = False
	
	try:
		#ouverture du fichier
		with open(const.cheminFichierListeServeurCsv, 'r') as f:
			reader = csv.reader(f, delimiter=';')
			#la boucle parcours le CSV
			for row in reader:
				#on saute les entêtes du CSV
				if skipEnteteCsv == False:
					skipEnteteCsv = True
					continue
				else:
					#remplissage de la liste 'listeServeur' en fonction du CSV
					listeServeur.append({'type': row[0], 'hostname': row[1], 'domaine' : row[2], 'groupe' : row[3]})
		
		print "SUCCES - Recuperation de la liste des serveurs du CSV"
		print " "
		
	except Exception as e:
		#Exception si probleme de lecture du fichier CSV qui contient la liste des serveurs à contacter
		print "ERROR - Probleme d'ouverture de la liste des serveurs (fichier CSV)"
		print "Erreur : " + str(e)
		print "Chemin du fichier : " + const.cheminFichierListeServeurCsv
		
		#fin du programme
		print ""
		print "ERROR - FIN PROGRAMME AUDIT"
		exit()
	
	else:
		#On retourne la liste des serveurs avec leurs détails (domaine, groupe, etc)
		return listeServeur