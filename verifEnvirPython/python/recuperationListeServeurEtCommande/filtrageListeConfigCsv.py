#!/usr/bin/python
# -*- coding: utf-8 -*-

################ Recuperation des elements nécessaires pour ce scénario ################
def funcFiltrageListeConfigCsv(listeServeur,listeGroupeCommandes,listeCommandes,scenario):
	################ SERVEURS ################
	listeServeurFiltre = []
	for ls in listeServeur:
		#On récupère les serveurs demandé en option
		if scenario["groupeServeurs"] == "" or ls["groupe"] in scenario["groupeServeurs"]:
			#remplissage de la liste 'listeServeurFiltre' en fonction du CSV
			listeServeurFiltre.append({'type': ls['type'], 'hostname': ls['hostname'], 'domaine' : ls['domaine'], 'groupe' : ls['groupe']})
	
	################ GROUPE COMMANDE ################
	listeGroupeCommandesFiltre = []
	for lg in listeGroupeCommandes:
		#Récupération des groupes parents (avec le séparateur ",")
		for grpParent in lg['grpParent'].split(","):
			#On récupère les groupes de commandes demandés
			if scenario["groupeCommandes"] == "" or grpParent in scenario["groupeCommandes"]:
				for grpEnfant in lg['grpEnfant'].split(","):
					if grpEnfant not in listeGroupeCommandesFiltre:
						#remplissage de la liste 'listeGroupeCommandesFiltre' en fonction du CSV
						listeGroupeCommandesFiltre.append(grpEnfant)
	
	################ COMMANDES ################
	listeCommandesFiltre = []
	for lg in listeCommandes:
		#On récupère les serveurs demandé en option
		if lg['groupeCommande'] in listeGroupeCommandesFiltre:
			listeCommandesFiltre.append({'libelle': lg['libelle'],'execution': lg['execution'], 'typeVerification': lg['typeVerification'], 'resultatAttendu' : lg['resultatAttendu'], 'marge' : lg['marge'], 'groupeCommande' : lg['groupeCommande']})
	
	#On retourne la liste des commandes avec leurs détails
	return {'listeServeurFiltre':listeServeurFiltre,
			'listeCommandesFiltre':listeCommandesFiltre}