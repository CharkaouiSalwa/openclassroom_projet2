# openclassroom_projet2
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

## Projet 2 : Utilisez les bases de Python pour l'analyse de marché
Ce projet sert à suivre manuellement les prix des livres sur un sites web http://books.toscrape.com/ d’un concurrent, il y a trop de livres et trop de librairies en ligne l’objectif d'automatiser cette tâche laborieuse via un programme (un scraper) développé en Python, capable d'extraire les informations tarifaires d'autres librairies en ligne.

 ### prérequis :
Avoir l'anacondas sur votre pc pour permettre d'utiliser la commande pip

## *l'installation de Python*

#### *Visitez le lien suivant* :   [Python](https://www.python.org/downloads/)
#### *ou bien utilisez le terminal* :

```
pip install Python
```
Après l'installation, téléchargez le repo sur  [Github](https://github.com/CharkaouiSalwa/openclassroom_projet2) 
Extraire le fichier telechargé, puis accéder au dossier du projet en ligne de commande:
```
cd openclassroom_projet2 
```
Créer l'environnement virtuel avec la commande :
```
python -m venv env
```
Activer votre environnement :
```
source  env/bin/activate
```
Installer automatiquements les bibliothéques mentionés sur le fichier avec la commande :
```
pip install -r requirements.txt
```
Copier le lien d'un livre depuis le site http://books.toscrape.com/index.html et le coller sur le script1 .
exemple d'un livre :
```
create_csv("https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html")
```
Exécution du script1 :
```
python script1.py
```

## Résultat :
* Un dossier "openclassroom_projet2" contenant :
    * dossier csv contient le résultat d'exécution d'un seul livre, d'une catégorie, et aprés tous les livres de toute les catégories
    * dossier images contient les images de tous les livres
## Contenu du repository github: 
* fichier sript1.py
* fichier script2.py
* fichier script3.py
* fichier requirements.txt
* fichier README.md
* fichier .gitignore





 



