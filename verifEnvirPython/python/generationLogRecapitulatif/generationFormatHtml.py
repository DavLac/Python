#!/usr/bin/python
# -*- coding: utf-8 -*-

#Import nécessaire pour utiliser les fonctions de cette fonction
from constantes.constantes import constanteStructure as const
from datetime import datetime

################ Génération du tableau recapitulatif des commandes au format HTML ################
def funcGenerationFormatHtml(timeNow,tabRecapFinal):

	print ""
	print "DEBUT - construction tableau recapitulatif"
	print "Format demande : HTML"
	
	#modification du format de la date récupérée "2018-01-30_12-50-22" en "30/01/2018 a 12h50m22s" (pour l'intérieur du fichier bilan généré)
	timeNowFormat = datetime.strptime(timeNow, "%Y-%m-%d_%H-%M-%S")
	timeNowFormat = timeNowFormat.strftime("%d/%m/%Y a %Hh%Mm%Ss")
	
	#Détermination du chemin et nom du fichier recap
	nomFichierFinal = "tableauRecapitulatif_" + timeNow + ".html"
	cheminEtNomFichierFinal = const.cheminTableauRecapitulatif + "/" + nomFichierFinal

	try:
		#creation du fichier recapitulatif
		file = open(cheminEtNomFichierFinal, mode="w")

	except Exception as e:
		#Exception si probleme de creation du fichier
		print "ERROR - Probleme de creation du fichier recapitulatif"
		print "Erreur : " + str(e)
		print "Chemin du fichier : " + cheminEtNomFichierFinal
		
	else:
		#Remplissage du fichier
		#En tete du fichier (HTML)
		file.write(const.DebutHtmlTableauRecapitulatif) 

		#Rajout de la date dans le HTML
		file.write("<h2>Resultat Audit du " + timeNowFormat + "</h2>")
		
		#On boucle sur chaque élément du scénario
		for index, tabRecap in enumerate(tabRecapFinal):
			file.write("<hr><h4>SCENARIO ['" + str(tabRecapFinal[index][0]["libelleScenario"]) + "'] SERVEURS " + str(tabRecapFinal[index][0]["groupeServeurs"]) + " COMMANDES " + str(tabRecapFinal[index][0]["groupeCommandes"]) + "</h4>")
			
			#Remplissage du contenu du tableau
			#compteur par boucle pour afficher les serveurs par groupe
			cpt = 0
			compteurEntreeTab = 0
			
			#une boucle par serveur
			for tabRec in tabRecap:
				#Si le serveur ne renvoi pas de commande, on affiche une erreur
				if tabRec["etat"] == "":
					messageSupplementaireBandeauServeur = ""
				elif tabRec["etat"] == "Aucune commande declaree":
					messageSupplementaireBandeauServeur = " Aucune commande declaree"
					compteurEntreeTab = compteurEntreeTab + 1
				elif tabRec["etat"] == "Problème de connexion":
					messageSupplementaireBandeauServeur = " Probleme de connexion au serveur"	
					compteurEntreeTab = compteurEntreeTab + 1
				
				#On affiche pas le bandeau du serveur s'il n'a aucune erreur
				if tabRec["etat"] != "Aucune commande en erreur":
					#1er groupe - 1er serveur OU groupe précédent est différent
					if cpt == 0 or tabRecap[cpt]["groupeServeur"] != tabRecap[(cpt-1)]["groupeServeur"]:
						file.write("<h4>" + tabRec["groupeServeur"] + "</h4>")
					cpt = cpt + 1
					
					#permet de gérer l'espace entre les groupes
					sautEntreGroupe = ""
					
					#calcul pourcentage final
					if tabRec["nombreCommandeTotal"] > 0:
						pourcentReussiteAuditFinal = 100*tabRec["nombreCommandeValide"]/tabRec["nombreCommandeTotal"]
					else:
						pourcentReussiteAuditFinal = 0

					#couleur de fond des lignes des serveurs en fonction pourcentage
					if pourcentReussiteAuditFinal == 100:
						cssCouleurPourcent = "vert"
					elif pourcentReussiteAuditFinal > 75:
						cssCouleurPourcent = "vertclair"
					elif pourcentReussiteAuditFinal > 50:
						cssCouleurPourcent = "jaune"
					elif pourcentReussiteAuditFinal > 25:
						cssCouleurPourcent = "orange"
					else:
						cssCouleurPourcent = "rouge"
					
					#Rajout du bandeau accordeon par serveur (HTML)
					file.write("""<button class="accordion """ + cssCouleurPourcent + """" """ + sautEntreGroupe + """>""" + tabRec["hostnameServeur"] + """ - """ + str(pourcentReussiteAuditFinal) + """% (""" + str(tabRec["nombreCommandeValide"]) + """/""" + str(tabRec["nombreCommandeTotal"]) + messageSupplementaireBandeauServeur + """)</button>
						<div class="panel">
						  <table>
							   <tr>
								   <th>Libelle commande</th>
								   <th>Retour commande</th>
								   <th>Resultat attendu</th>
								   <th>OK/NOK</th>
							   </tr>""")
							   
					#Remplissage du tableau avec le détail des commandes
					#une boucle pour x commande pour y serveur
					for tabResult in tabRec["listeResultatCommande"]:
					
						#Compte le nombre d'entrée dans le tableau
						compteurEntreeTab = compteurEntreeTab + 1
						
						#Couleur des commandes en erreur (en rouge en CSS)
						if tabResult["verifCommande"] == "OK":
							cssErrorColor = ""
						else:
							cssErrorColor = ' style="color:red"'
						
						#affichage de la marge si c'est une vérification avec marge
						if tabResult["typeVerification"] == "NombreAvecMarge":
							afficherMarge = " (marge: " + tabResult["marge"] + "%)"
						else:
							afficherMarge = ""
						
						#Rajout ligne par ligne du recap des commandes
						file.write("""<tr""" + cssErrorColor + """>
							   <td>""" + tabResult["libelleCommande"] + """</td>
							   <td>""" + tabResult["retourCommande"] + """</td>
							   <td>""" + tabResult["resultatAttendu"] + afficherMarge + """</td>
							   <td>""" + tabResult["verifCommande"] + """</td></tr>""")
									
					file.write("</table></div>")
		
		#Si le tableau ne renvoi rien, on affiche un message
		if compteurEntreeTab == 0:
			file.write('<h4 style="color:red">Aucun resultat a afficher</h4>')

		#Fin du fichier (partie javascript)
		file.write(const.FinHtmlTableauRecapitulatif)
		
		#Fermeture du fichier
		file.close()
		
		print ">>> Fichier " + nomFichierFinal + " a ete cree et place a cet emplacement : " + const.cheminTableauRecapitulatif
		print "SUCCES - construction tableau recapitulatif au format HTML"