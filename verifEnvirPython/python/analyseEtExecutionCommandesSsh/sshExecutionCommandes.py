#!/usr/bin/python
# -*- coding: utf-8 -*-

#Import nécessaire pour utiliser les fonctions de cette fonction
from constantes.constantes import constanteStructure as const
import connexionSSH as connect
import verificationStructureCommande as verifstruc
import analyseRetourCommandes as anaRet

################ Fonction qui exécute les commandes en fonction des groupes des serveurs ################
def funcSshExecutionCommandes(listeServeur, listeCommandes, commandeType, scenario):
	
	print "DEBUT - Lancement des commandes en SSH"
	#Initialisation du tableau qui contiendra toutes les informations (serveurs + commandes + résultat des commandes)
	tabRecap = []
	
	#boucle qui parcours la liste des serveurs
	for serveurInfo in listeServeur:
		
		################ Connexion SSH sur chacun des serveurs ################
		print '################# Groupe ' + serveurInfo["groupe"] + ' - Serveur ' + serveurInfo["hostname"] + ' #################'
		
		#tableau qui va récupérer le résultat des commandes du CSV
		tabResultcom = []
		problemeConnexion = False
		
		#on récupère le hostname du serveur que l'on va contacter
		hostname = serveurInfo["hostname"] + "." + serveurInfo["domaine"]
		#établissement de la connexion SSH au serveur "hostname" avec l'utilisateur "root" et sa clé privée
		resultFunc = connect.funcConnexionSSH(hostname,"root",const.cheminClePrivee)
		
		#On récupère le retour de la fonction "funcConnexionSSH"
		#on récupère le client pour executer les commandes plus tard
		if "client" in resultFunc:
			clientSsh = resultFunc["client"]
		#Et les erreurs s'il y en a
		if "resultatCommandeErreur" in resultFunc:
			tabResultcom.append(resultFunc["resultatCommandeErreur"])
			problemeConnexion = True
		
		#initialisation des compteurs des commandes
		nbCommandeParHostnameValide = 0
		nbCommandeParHostnameTotal = 0
		
		#On est bien connecté au serveur, on peut analyser les commandes
		if problemeConnexion == False:
			#compteur numéro de ligne des commandes dans le fichier
			numLigneCommande = 2
			
			#boucle qui parcours les commandes de la liste des commandes
			for listCmd in listeCommandes:
			
				################ Vérification des commandes ################
				#Fonction de vérification de la structure de chaque commande. S'il manque un élément obligatoire d'une commande, une erreur est affichée.
				resultFunc = verifstruc.funcVerificationStructureCommande(listCmd,numLigneCommande)
				
				#### On récupère le retour de la fonction "funcVerificationStructureCommande"
				#Booléen qui indique si la commande a une structure correcte (true) ou non (false)
				structureCommandeCorrect = resultFunc["structureCommandeCorrect"]
				#Et les erreurs s'il y en a
				if "resultatCommandeErreur" in resultFunc:
					nbCommandeParHostnameTotal = nbCommandeParHostnameTotal + 1
					tabResultcom.append(resultFunc["resultatCommandeErreur"])
				
				###### Suite du programme
				###### Commandes avec une structure correcte. On peut commencer à executer les commandes vers les serveurs
				if structureCommandeCorrect:
					try:
						############### Execution des commandes
						stdin , stdout, stderr = clientSsh.exec_command(listCmd["execution"])
						resultatCommande = stdout.read()
						
						#on enlève le retour à la ligne du résultat des commandes
						resultatCommande = resultatCommande.replace("\n", "")
						
					except Exception as e:
						#Exception si la commande a un probleme inconnu
						erreur =  "ERROR : la commande '" + listCmd["libelle"] + "' a eu un probleme lors de son execution."
						nbCommandeParHostnameTotal = nbCommandeParHostnameTotal + 1
						#tabResultcom.append(result.resultatCommande(listCmd["libelle"], erreur,"","NOK","","",""))
						tabResultcom.append({'libelleCommande': listCmd["libelle"],'retourCommande': erreur, 'resultatAttendu': "", 'verifCommande' : "NOK", 'typeVerification' : "", 'marge' : ""})
						print erreur
						
					else:
						#Il n'y a pas d'erreur d'execution, on peut analyser le résultat de la commande
						
						##### ANALYSE DU RESULTAT
						#Fonction d'analyse des résultat en fonction du type des commandes
						resultFunc = anaRet.funcAnalyseRetourCommandes(resultatCommande,listCmd,nbCommandeParHostnameTotal,nbCommandeParHostnameValide,commandeType)
						
						#Récupération des variables de la fonction funcAnalyseRetourCommandes
						nbCommandeParHostnameTotal = resultFunc["nbCommandeParHostnameTotal"]
						nbCommandeParHostnameValide = resultFunc["nbCommandeParHostnameValide"]
						if "retourResultatAnalyse" in resultFunc:
							tabResultcom.append(resultFunc["retourResultatAnalyse"])
								
				#On incrémente le numéro des lignes correspondant au CSV
				numLigneCommande = numLigneCommande + 1
				
			#fermeture de la connexion SSH
			clientSsh.close()
		
		#Rajout de précisions sur l'état du serveur
		if problemeConnexion == True:
			etatServeur = "Problème de connexion"
		elif commandeType == "error" and nbCommandeParHostnameTotal == 0:
			etatServeur = "Aucune commande en erreur"
			print etatServeur
		elif commandeType == "all" and nbCommandeParHostnameTotal == 0:
			etatServeur = "Aucune commande declaree"
			print etatServeur
		else:
			etatServeur = ""
		
		#On rempli l'objet qui va permettre de créer le tableau recapitulatif
		tabRecap.append({'groupeServeur': serveurInfo["groupe"],'hostnameServeur': serveurInfo["hostname"], 'listeResultatCommande': tabResultcom, 'nombreCommandeTotal' : nbCommandeParHostnameTotal, 'nombreCommandeValide' : nbCommandeParHostnameValide, 'etat' : etatServeur, 'libelleScenario' : scenario['libelleScenario'], 'groupeServeurs' : scenario['groupeServeurs'], 'groupeCommandes' : scenario['groupeCommandes']})
			
	print "SUCCES - Lancement des commandes en SSH"
	print ""
	
	#On retourne le tableau recapitulatif
	return tabRecap