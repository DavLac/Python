#!/usr/bin/python
# -*- coding: utf-8 -*-

#Import nécessaire pour utiliser les fonctions de cette fonction
import csv
from constantes.constantes import constanteStructure as const

################ Fonction recuperation de la liste des groupe de commandes du CSV ################
def funcRecuperationListeGroupeCommandes():

	#initialisation du tableau qui recevra la liste des groupe de commandes
	listeGroupeCommandes = []
	
	print "DEBUT - Recuperation de la liste des groupe de commandes du CSV"
	print "Fichier : " + const.cheminFichierListeGroupeCommandesCsv
	
	#Cette variable permet de sauter la première ligne du CSV pour ne pas prendre en compte les en-tete
	skipEnteteCsv = False
	
	try:
		#ouverture du fichier
		with open(const.cheminFichierListeGroupeCommandesCsv, 'r') as f:
			reader = csv.reader(f, delimiter=';')
			#la boucle parcours le CSV
			for row in reader:
				#on saute les entêtes du CSV
				if skipEnteteCsv == False:
					skipEnteteCsv = True
					continue
				else:
					#On récupère les groupes de commandes
					listeGroupeCommandes.append({'grpParent': row[0],'grpEnfant': row[1]})
		
		print "SUCCES - Recuperation de la liste des groupe de commandes du CSV"
		print " "
	
	except Exception as e:
		#Exception si probleme de lecture du JSON des commandes
		print "ERROR - Probleme d'ouverture de la liste des groupes de commandes (fichier CSV)"
		print "Erreur : " + str(e)
		print "Chemin du fichier : " + const.cheminFichierListeGroupeCommandesCsv
		
		#fin du programme
		print ""
		print "ERROR - FIN PROGRAMME AUDIT"
		exit()
	
	else:
		#On retourne la liste des commandes avec leurs détails
		return listeGroupeCommandes