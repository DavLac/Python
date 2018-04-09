#!/usr/bin/python
# -*- coding: utf-8 -*-

#Import nécessaire pour utiliser les fonctions de cette fonction
from recuperationListeServeurEtCommande import recuperationListeScenarios as recScen
from recuperationListeServeurEtCommande import recuperationListeServeurs as recServ
from recuperationListeServeurEtCommande import recuperationListeCommandes as recCom
from recuperationListeServeurEtCommande import recuperationListeGroupeCommandes as recGrCom

################ Recuperation des données CSV ################
def funcRecuperationCsv(libelleScenario):	
	listeScenario = recScen.recuperationListeScenarios(libelleScenario)
	listeServeur = recScen.recuperationListeServeurs()
	listeCommandes = recScen.recuperationListeCommandes()
	listeGroupeCommandes = recScen.recuperationListeGroupeCommandes()
	
	#On retourne l'objet
	return {'listeScenario':listeScenario,
			'listeServeur':listeServeur,
			'listeCommandes':listeCommandes,
			'listeGroupeCommandes':listeGroupeCommandes}