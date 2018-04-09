#!/usr/bin/python
# -*- coding: utf-8 -*-

##### ANALYSE DU RESULTAT
def funcAnalyseRetourCommandes(resultatCommande,listCmd,nbCommandeParHostnameTotal,nbCommandeParHostnameValide,commandeType):
			
	#VERIFICATION - type Nombre avec marge
	if listCmd["typeVerification"] == "NombreAvecMarge":
		if float(resultatCommande) <= float(listCmd["resultatAttendu"])*((100 + float(listCmd["marge"]))/100) and float(resultatCommande) >= float(listCmd["resultatAttendu"])*((100 - float(listCmd["marge"]))/100):
			retourResultat = "OK"
			verifCommande = True
		else:
			retourResultat = "NOK"
			verifCommande = False
			
		#Affichage du résultat pour le tableau recapitulatif
		if commandeType == "all" or (commandeType == "error" and verifCommande == False):
			retourResultatAnalyse = {'libelleCommande': listCmd["libelle"],'retourCommande': resultatCommande, 'resultatAttendu': listCmd["resultatAttendu"], 'verifCommande' : retourResultat, 'typeVerification' : listCmd["typeVerification"], 'marge' : listCmd["marge"]}
	
	#VERIFICATION - type EgalAvecTri
	elif listCmd["typeVerification"] == "EgaliteListeSeparateurVirgule":
		#On split sur les virgules ET on tri PUIS 
		#on vérifie l'égalité du retour du serveur en gérant les caractères spéciaux (unicode)
		
		#Recuperation du résultat attendu en traduisant en UTF8
		resultatAttendu = str(unicode(listCmd["resultatAttendu"], errors='ignore'))
		#Split selon les virgules puis tri
		resultatAttendu = resultatAttendu.split(",")
		resultatAttendu.sort()
		resultatAttenduApresTri = ""
		#Parcours du tableau trié pour le concaténer dans une nouvelle chaine
		for resAtt in resultatAttendu:
			resultatAttenduApresTri = resultatAttenduApresTri + "," + resAtt
		
		#Recuperation du retour du serveur en traduisant en UTF8
		resultatCommandeServeur = str(unicode(resultatCommande, errors='ignore'))
		#Split selon les virgules puis tri
		resultatCommandeServeur = resultatCommandeServeur.split(",")
		resultatCommandeServeur.sort()
		resultatCommandeServeurApresTri = ""
		#Parcours du tableau trié pour le concaténer dans une nouvelle chaine
		for resCom in resultatCommandeServeur:
			resultatCommandeServeurApresTri = resultatCommandeServeurApresTri + "," + resCom
		
		if resultatAttenduApresTri == resultatCommandeServeurApresTri:
			retourResultat = "OK"
			verifCommande = True
		else:
			retourResultat = "NOK"
			verifCommande = False
			
		#Affichage du résultat pour le tableau recapitulatif
		if commandeType == "all" or (commandeType == "error" and verifCommande == False):
			retourResultatAnalyse = {'libelleCommande': listCmd["libelle"],'retourCommande': resultatCommande, 'resultatAttendu': listCmd["resultatAttendu"], 'verifCommande' : retourResultat, 'typeVerification' : listCmd["typeVerification"], 'marge' : ""}
	
	#VERIFICATION - type Egalite
	elif listCmd["typeVerification"] == "Egal":
		#On vérifie l'égalité du retour du serveur en gérant les caractères spéciaux (unicode)
		if unicode(listCmd["resultatAttendu"], errors='ignore') == unicode(resultatCommande, errors='ignore'):
			retourResultat = "OK"
			verifCommande = True
		else:
			retourResultat = "NOK"
			verifCommande = False
			
		#Affichage du résultat pour le tableau recapitulatif
		if commandeType == "all" or (commandeType == "error" and verifCommande == False):
			retourResultatAnalyse = {'libelleCommande': listCmd["libelle"],'retourCommande': resultatCommande, 'resultatAttendu': listCmd["resultatAttendu"], 'verifCommande' : retourResultat, 'typeVerification' : listCmd["typeVerification"], 'marge' : ""}
	
	#VERIFICATION - type NON Egalite
	elif listCmd["typeVerification"] == "NonEgal":
		if unicode(listCmd["resultatAttendu"], errors='ignore') == unicode(resultatCommande, errors='ignore'):
			retourResultat = "NOK"
			verifCommande = False
		else:
			retourResultat = "OK"
			verifCommande = True
		
		#Affichage du résultat pour le tableau recapitulatif
		if commandeType == "all" or (commandeType == "error" and verifCommande == False):
			retourResultatAnalyse = {'libelleCommande': listCmd["libelle"],'retourCommande': resultatCommande, 'resultatAttendu': "Ne doit pas etre egal a : '" + listCmd["resultatAttendu"] + "'", 'verifCommande' : retourResultat, 'typeVerification' : listCmd["typeVerification"], 'marge' : ""}
	
	#VERIFICATION - type NonNull
	elif listCmd["typeVerification"] == "NonNull":
		if resultatCommande == "" or resultatCommande is None:
			retourResultat = "NOK"
			verifCommande = False
		else:
			retourResultat = "OK"
			verifCommande = True
		
		#Affichage du résultat pour le tableau recapitulatif
		if commandeType == "all" or (commandeType == "error" and verifCommande == False):
			retourResultatAnalyse = {'libelleCommande': listCmd["libelle"],'retourCommande': resultatCommande, 'resultatAttendu': "La commande attend un retour", 'verifCommande' : retourResultat, 'typeVerification' : listCmd["typeVerification"], 'marge' : ""}
	
	#VERIFICATION - type Null
	elif listCmd["typeVerification"] == "Null":
		if resultatCommande == "" or resultatCommande is None:
			retourResultat = "OK"
			verifCommande = True
		else:
			retourResultat = "NOK"
			verifCommande = False
		
		#Affichage du résultat pour le tableau recapitulatif
		if commandeType == "all" or (commandeType == "error" and verifCommande == False):
			retourResultatAnalyse = {'libelleCommande': listCmd["libelle"],'retourCommande': resultatCommande, 'resultatAttendu': "La commande n'attend pas de retour", 'verifCommande' : retourResultat, 'typeVerification' : listCmd["typeVerification"], 'marge' : ""}

	else:
		#Exception si une commande a un champ "typeVerification" non pris en charge
		erreur = "ERROR : la commande '" + listCmd["libelle"] + "' a un champ 'typeVerification' non pris en charge par le programme ('" + listCmd["typeVerification"] + "'). Merci de le modifier."
		nbCommandeParHostnameTotal = nbCommandeParHostnameTotal + 1
		retourResultatAnalyse = {'libelleCommande': listCmd["libelle"],'retourCommande': erreur, 'resultatAttendu': "", 'verifCommande' : "NOK", 'typeVerification' : "", 'marge' : ""}
		print erreur
	
	#Vérification si la commande est en succes avec afficahge des logs et incrément des compteurs
	if verifCommande == True and commandeType == "all":
		print 'SUCCESS : ' + listCmd["libelle"]
		nbCommandeParHostnameTotal = nbCommandeParHostnameTotal + 1
		nbCommandeParHostnameValide = nbCommandeParHostnameValide + 1
	elif verifCommande == False:
		print 'ERROR : ' + listCmd["libelle"]
		nbCommandeParHostnameTotal = nbCommandeParHostnameTotal + 1
	
	#Si la commande retourne un résultat correct et qu'on veut afficher que les erreurs, on enlève la variable "retourResultatAnalyse" du "return" de la fonction
	if verifCommande == True and commandeType == "error":
		return {'nbCommandeParHostnameTotal':nbCommandeParHostnameTotal,
			'nbCommandeParHostnameValide':nbCommandeParHostnameValide}
	else:
		return {'nbCommandeParHostnameTotal':nbCommandeParHostnameTotal,
			'nbCommandeParHostnameValide':nbCommandeParHostnameValide,
			'retourResultatAnalyse':retourResultatAnalyse}