#!/usr/bin/python
# -*- coding: utf-8 -*-

#Import nécessaire pour utiliser les fonctions de cette fonction
import csv
from constantes.constantes import constanteStructure as const

################ Fonction recuperation de la liste des scenarios du CSV ################
def funcRecuperationListeScenario(groupeScenario):

	#initialisation du tableau qui recevra la liste des scenarios
	listeScenario = []
	
	print "DEBUT - Recuperation de la liste des scenarios du CSV"
	print "Fichier : " + const.cheminFichierListeScenarioCsv
	
	#Cette variable permet de sauter la première ligne du CSV pour ne pas prendre en compte les en-tete
	skipEnteteCsv = False
	
	try:
		#ouverture du fichier
		with open(const.cheminFichierListeScenarioCsv, 'r') as f:
			reader = csv.reader(f, delimiter=';')
			#la boucle parcours le CSV
			for row in reader:
				#on saute les entêtes du CSV
				if skipEnteteCsv == False:
					skipEnteteCsv = True
					continue
				else:
					#On récupère les groupes de commandes demandés
					if groupeScenario == "" or row[0] in groupeScenario:
						#remplissage de la liste 'listeScenario' en fonction du CSV
						listeScenario.append({'libelleScenario': row[0], 'groupeServeurs': row[1].split(","),'groupeCommandes': row[2].split(",")})
		
		print "SUCCES - Recuperation de la liste des scenarios du CSV"
		print " "
	
	except Exception as e:
		#Exception si probleme de lecture du CSV
		print "ERROR - Probleme d'ouverture de la liste des scenarios (fichier CSV)"
		print "Erreur : " + str(e)
		print "Chemin du fichier : " + const.cheminFichierListeScenarioCsv
		
		#fin du programme
		print ""
		print "ERROR - FIN PROGRAMME AUDIT"
		exit()
	
	else:
		#On retourne la liste des commandes avec leurs détails
		return listeScenario