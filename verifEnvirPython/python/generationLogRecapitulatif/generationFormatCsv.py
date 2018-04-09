#!/usr/bin/python
# -*- coding: utf-8 -*-

#Import nécessaire pour utiliser les fonctions de cette fonction
from constantes.constantes import constanteStructure as const
import csv

################ Génération du tableau recapitulatif des commandes au format CSV ################
def funcGenerationFormatCsv(timeNow,tabRecapFinal):
	
	print ""
	print "DEBUT - construction tableau recapitulatif"
	print "Format demande : CSV"
	
	#Détermination du chemin et nom du fichier recap
	nomFichierFinal = "tableauRecapitulatif_" + timeNow + ".csv"
	cheminEtNomFichierFinal = const.cheminTableauRecapitulatif + "/" + nomFichierFinal
	
	with open(cheminEtNomFichierFinal, 'wb') as csvfile:
		filewriter = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		filewriter.writerow(['Groupe serveur', 'Hostname serveur', 
							'Libelle commande', 'Retour commande',
							'Resultat attendu','OK/NOK'])
		
		#On boucle sur chaque élément du scénario
		for tabRecap in tabRecapFinal:
			compteurEntreeTab = 0
			
			#une boucle par serveur
			for tabRec in tabRecap:
				#une boucle pour x commande pour y serveur
				for tabResult in tabRec["listeResultatCommande"]:
					
					#Compte le nombre d'entrée dans le tableau
					compteurEntreeTab = compteurEntreeTab + 1
					
					#affichage de la marge si c'est une vérification avec marge
					if tabResult["typeVerification"] == "NombreAvecMarge":
						afficherMarge = " (marge: " + tabResult["marge"] + "%)"
					else:
						afficherMarge = ""
					
					filewriter.writerow([tabRec["groupeServeur"], tabRec["hostnameServeur"],
									tabResult["libelleCommande"], tabResult["retourCommande"],
									tabResult["resultatAttendu"] + afficherMarge, tabResult["verifCommande"]])
								
		#Si le tableau ne renvoi rien, on affiche un message
		if compteurEntreeTab == 0:
			filewriter.writerow(["Aucun resultat a afficher"])
	
	print ">>> Fichier " + nomFichierFinal + " a ete cree et place a cet emplacement : " + const.cheminTableauRecapitulatif
	print "SUCCES - construction tableau recapitulatif au format CSV"