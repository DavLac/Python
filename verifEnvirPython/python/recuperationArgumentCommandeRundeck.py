#!/usr/bin/python
# -*- coding: utf-8 -*-

#Import nécessaire pour utiliser les fonctions de cette fonction
import os

################ Recuperation des arguments de la commande Rundeck ################
def funcRecuperationArgumentCommandeRundeck():
	#OPTION : Option-de-traitement (affiche tout ou juste les erreurs)
	if os.environ.get('RD_OPTION_OPTION_DE_TRAITEMENT') == "Afficher-les-commandes-en-erreur":
		commandeType = "error"
	elif os.environ.get('RD_OPTION_OPTION_DE_TRAITEMENT') == "Afficher-toutes-les-commandes":
		commandeType = "all"
		
	#OPTION : groupes-commande (permet de filtrer les commandes que l'on veut executer)
	if os.environ.get('RD_OPTION_SCENARIO') != None:
		libelleScenario = os.environ.get('RD_OPTION_SCENARIO').split(';')
	else:
		libelleScenario = ""
		
	#On retourne l'objet de connexion
	return {'commandeType':commandeType,
			'libelleScenario':libelleScenario}