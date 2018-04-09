#!/usr/bin/python
# -*- coding: utf-8 -*-

class constanteStructure:
	cheminFichierListeServeurCsv = 'projects/Source_Solde/scripts/envir_check/verifEnvirPython/listeServeurs.csv'
	cheminFichierListeCommandesCsv = 'projects/Source_Solde/scripts/envir_check/verifEnvirPython/listeCommandes.csv'
	cheminFichierListeGroupeCommandesCsv = 'projects/Source_Solde/scripts/envir_check/verifEnvirPython/listeGroupeCommandes.csv'
	cheminFichierListeScenarioCsv = 'projects/Source_Solde/scripts/envir_check/verifEnvirPython/listeScenario.csv'

	#Chemin clé privée sur le serveur "slnxsosoinstall.ptx.fr.sopra" > "~/.ssh/id_rsa"
	#Permet de se connecter automatiquement grace à la clé publique du serveur "slnxsosoinstall" enregistrée dans le dossier "~/.ssh/authorized_key" du serveur cible
	cheminClePrivee = "../../../../root/.ssh/id_rsa"

	cheminTableauRecapitulatif = 'projects/Source_Solde/scripts/envir_check/verifEnvirPython/logRecapitulatif'

	DebutHtmlTableauRecapitulatif = """
	<!DOCTYPE html>
	<html>
		<head>
			<style>
				body{
					background-color: #f2f2f2;
				}
				
				.accordion {
					background-color: #eee;
					color: #444;
					cursor: pointer;
					padding: 18px;
					width: 100%;
					border: none;
					text-align: left;
					outline: none;
					font-size: 15px;
					transition: 0.4s;
				}
				
				.rouge {
					background-color: #f8696b;
				}
				
				.orange {
					background-color: #ffb985;
				}
				
				.jaune {
					background-color: #ffeb84;
				}
				
				.vertclair {
					background-color: #a1d34f;
				}
				
				.vert {
					background-color: #63be7b;
				}

				.active, .accordion:hover {
					background-color: #ccc; 
				}

				.panel {
					padding: 0 18px;
					display: none;
				}
				table a:link {
					color: #666;
					font-weight: bold;
					text-decoration:none;
				}
				table a:visited {
					color: #999999;
					font-weight:bold;
					text-decoration:none;
				}
				table a:active,
				table a:hover {
					color: #bd5a35;
					text-decoration:underline;
				}
				table {
					font-family:Arial, Helvetica, sans-serif;
					color:#666;
					font-size:12px;
					text-shadow: 1px 1px 0px #fff;
					background:#eaebec;
					margin:20px;
					border:#ccc 1px solid;

					-moz-border-radius:3px;
					-webkit-border-radius:3px;
					border-radius:3px;

					-moz-box-shadow: 0 1px 2px #d1d1d1;
					-webkit-box-shadow: 0 1px 2px #d1d1d1;
					box-shadow: 0 1px 2px #d1d1d1;
				}
				table th {
					padding:21px 25px 22px 25px;
					border-top:1px solid #fafafa;
					border-bottom:1px solid #e0e0e0;

					background: #ededed;
					background: -webkit-gradient(linear, left top, left bottom, from(#ededed), to(#ebebeb));
					background: -moz-linear-gradient(top,  #ededed,  #ebebeb);
				}
				table th:first-child {
					text-align: left;
					padding-left:20px;
				}
				table tr:first-child th:first-child {
					-moz-border-radius-topleft:3px;
					-webkit-border-top-left-radius:3px;
					border-top-left-radius:3px;
				}
				table tr:first-child th:last-child {
					-moz-border-radius-topright:3px;
					-webkit-border-top-right-radius:3px;
					border-top-right-radius:3px;
				}
				table tr {
					text-align: center;
					padding-left:20px;
				}
				table td:first-child {
					text-align: left;
					padding-left:20px;
					border-left: 0;
				}
				table td {
					padding:18px;
					border-top: 1px solid #ffffff;
					border-bottom:1px solid #e0e0e0;
					border-left: 1px solid #e0e0e0;

					background: #fafafa;
					background: -webkit-gradient(linear, left top, left bottom, from(#fbfbfb), to(#fafafa));
					background: -moz-linear-gradient(top,  #fbfbfb,  #fafafa);
				}
				table tr.even td {
					background: #f6f6f6;
					background: -webkit-gradient(linear, left top, left bottom, from(#f8f8f8), to(#f6f6f6));
					background: -moz-linear-gradient(top,  #f8f8f8,  #f6f6f6);
				}
				table tr:last-child td {
					border-bottom:0;
				}
				table tr:last-child td:first-child {
					-moz-border-radius-bottomleft:3px;
					-webkit-border-bottom-left-radius:3px;
					border-bottom-left-radius:3px;
				}
				table tr:last-child td:last-child {
					-moz-border-radius-bottomright:3px;
					-webkit-border-bottom-right-radius:3px;
					border-bottom-right-radius:3px;
				}
				table tr:hover td {
					background: #f2f2f2;
					background: -webkit-gradient(linear, left top, left bottom, from(#f2f2f2), to(#f0f0f0));
					background: -moz-linear-gradient(top,  #f2f2f2,  #f0f0f0);	
				}
				h2,h4{
					font-family:Arial, Helvetica, sans-serif;
					color : #404040;
				}
			</style>
		</head>
		<body>
	"""

	FinHtmlTableauRecapitulatif = """
	<script>
				var acc = document.getElementsByClassName("accordion");
				var i;

				for (i = 0; i < acc.length; i++) {
					acc[i].addEventListener("click", function() {
						this.classList.toggle("active");
						var panel = this.nextElementSibling;
						if (panel.style.display === "block") {
							panel.style.display = "none";
						} else {
							panel.style.display = "block";
						}
					});
				}
			</script>

		</body>
	</html>
	"""