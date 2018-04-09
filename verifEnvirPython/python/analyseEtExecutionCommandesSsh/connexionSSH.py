#!/usr/bin/python
# -*- coding: utf-8 -*-

#Import nécessaire pour utiliser les fonctions de cette fonction
from constantes.constantes import constanteStructure as const
import paramiko

################ Fonction connexion SSH ################
def funcConnexionSSH(hostnameServeur,login,clePrivee):

	try:
		#on récupère la clé privée du serveur 'slnxsosoinstall' pour s'authentifier automatiquement en SSH grace à sa clé publique qui est stockée sur le serveur cible dans ~/.ssh/authorized_key
		privateKey = paramiko.RSAKey.from_private_key_file(clePrivee)
		client = paramiko.SSHClient()
		client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			
		#Connexion SSH avec le compte root du serveur "slnxsosoinstall" et sa clé privée "privateKey"
		client.connect( hostname = hostnameServeur, username = login, pkey = privateKey )
	
	except Exception as e:
		#Exception si probleme de connexion à un serveur
		print hostnameServeur + " : Probleme de connexion au serveur !"
		#Si il y a un probleme de connexion SSH, on affiche le détail de l'exception dans le tableau final
		resultatCommandeErreur = {'libelleCommande': "Connexion SSH",'retourCommande': hostnameServeur + "<br/>" + str(e), 'resultatAttendu': "", 'verifCommande' : "NOK", 'typeVerification' : "", 'marge' : ""}
		#On retourne l'erreur pour l'afficher dans le tableau recapitulatif
		try:
			return {'client':client,'resultatCommandeErreur':resultatCommandeErreur}
		except Exception as e:
			#Exception s'il y a un probleme avec la clé privée utilisée pour s'authentifier au serveur
			print "Verifier si la cle privee du serveur est correcte : '" + const.cheminClePrivee + "'"
			#on retourne l'erreur sans le 'client' en erreur
			return {'resultatCommandeErreur':resultatCommandeErreur}
	else:
		#On retourne l'objet de connexion
		return {'client':client}