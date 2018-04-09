#!/usr/bin/python
# -*- coding: utf-8 -*-

################ Verification de la structure des commandes ################
#Vérification de la structure de chaque commande. S'il manque un élément obligatoire d'une commande, on le rajoute dans le tableau "listeElementManquantCommande" pour renvoyer une erreur par la suite.
def funcVerificationStructureCommande(listCmd,numLigneCommande):

	structureCommandeCorrect = True
	listeElementManquantCommande = []
	
	if listCmd["libelle"] == "":
		listeElementManquantCommande.append("libelle")
		structureCommandeCorrect = False
	elif listCmd["typeVerification"] == "":
		listeElementManquantCommande.append("execution")
		structureCommandeCorrect = False
	elif listCmd["typeVerification"] == "":
		listeElementManquantCommande.append("typeVerification")
		structureCommandeCorrect = False
	elif listCmd["resultatAttendu"] == "" and (listCmd["typeVerification"] == "Egal" or listCmd["typeVerification"] == "NonEgal" or listCmd["typeVerification"] == "NombreAvecMarge" or listCmd["typeVerification"] == "EgaliteListeSeparateurVirgule") :
		listeElementManquantCommande.append("resultatAttendu")
		structureCommandeCorrect = False
	elif listCmd["marge"] == "" and listCmd["typeVerification"] == "NombreAvecMarge" :
		listeElementManquantCommande.append("marge")
		structureCommandeCorrect = False
	
	#Si il y a un élément manquant dans la commande
	if structureCommandeCorrect == False:
		#Commande sans libelle en erreur
		if listCmd["libelle"] == "":
			erreur = "ERROR : la structure de la commande est incorrecte. Merci de rajouter le(s) champ(s) " + str(listeElementManquantCommande) + " dans la commande du CSV 'listeCommandes.csv'"
			resultatCommandeErreur = {'libelleCommande': "Commande ligne" + str(numLigneCommande),'retourCommande': erreur, 'resultatAttendu': "", 'verifCommande' : "NOK", 'typeVerification' : "", 'marge' : ""}
			#Affichage de l'erreur
			print erreur
			
		#Commande avec libelle en erreur
		else:
			erreur = "ERROR : la structure de la commande '" + listCmd["libelle"] + "' est incorrecte. Merci de rajouter le(s) champ(s) " + str(listeElementManquantCommande) + " dans la commande du CSV 'listeCommandes.csv' ligne " + str(numLigneCommande)
			resultatCommandeErreur = {'libelleCommande': listCmd["libelle"],'retourCommande': erreur, 'resultatAttendu': "", 'verifCommande' : "NOK", 'typeVerification' : "", 'marge' : ""}
			#Affichage de l'erreur
			print erreur
		
		#On retourne le booléen qui indique si la structure de la commande est correcte ainsi que l'erreur à afficher
		return {'structureCommandeCorrect':structureCommandeCorrect, 'resultatCommandeErreur':resultatCommandeErreur}
	else:
		#On retourne l'objet de connexion
		return {'structureCommandeCorrect':structureCommandeCorrect}