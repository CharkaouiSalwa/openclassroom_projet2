# openclassroom_projet2
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

## Projet 2 : Utilisez les bases de Python pour l'analyse de marché
  Ce projet sert à suivre manuellement les prix des livres sur un sites web http://books.toscrape.com/index.html d’un concurrent, il y a trop de livres et trop de librairies en ligne l’objectif d'automatiser cette tâche laborieuse via un programme (un scraper) développé en Python, capable d'extraire les informations tarifaires d'autres librairies en ligne.

 ### prérequis :
Avoir l'anacondas sur votre pc pour permettre d'utiliser la commande pip

## *l'installation de Python*

#### *Visitez le lien suivant* :   [Python](https://www.python.org/downloads/)
#### *ou bien utilisez le terminal* :

```
pip install Python
```
Aprés l'installations vous pouvez accédez au lien du  [Github](https://github.com/CharkaouiSalwa/openclassroom_projet2) 
pour le dossier Zip et l'extraire , vous pouvez les ouvrires à l'aide de python pour les consulter et aprés l'exécuter au terminal par la commande suivante : pour ouvrir le dossier
pour ouvrir le dossier :
```
cd openclassroom_projet2 
```
Pour afficher ce qui est dedans : 
```
ls
```
Aprés vous créez l'environnement virtuel avec la commande :
```
python -m venv env
```
Activer votre environnement :
```
source  env/bin/activate
```
Vous trouverez un fichier requièrement.txt qui contient tous les bibliothéques installés sur Python :
 - ouvrir le fichier requièrement.txt à l'aide du terminal
```
cd  requièrement.txt
```
 - Installer automatiquements les bibliothéque mentionés sur le fichier avec la commande
```pip install -r requirements.txt
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
Pour voir le résultat , vous acéder à votre dossier et vous cherchez un fihier csv , vous trouverez
un fihier one_book.csv  créer apres l'exécution pour le visiter :
 - aller vers un fichier exel vierge 
 - vous suivez les étapes su les images :

![This is an image](/Users/salwacharkaoui/Desktop/1.png)
![This is an image](/Users/salwacharkaoui/Desktop/2.png)
![This is an image](/Users/salwacharkaoui/Desktop/3.png)
 et aprés vous pouvez voir le résultat sur le tableau et cest la méme façon pour exécuter toutes les sriptes

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





 



