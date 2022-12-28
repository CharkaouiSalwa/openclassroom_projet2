# Projet 2 : Utilisez les bases de Python pour l'analyse de marché
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

## &ensp;&ensp;&ensp;Contexte :
Création d'un outil en langage Python permettant de récupérer des informations sur des articles comme le titre, le prix, la note etc.. sur les livres du site http://books.toscrape.com/. Cet outil permet également de récupérer les informations d'une catégorie voir de toutes les catégories disponibles et convertir les données dans un fichier CSV. Les images des articles consultés sont également téléchargées automatiquement.

## &ensp;&ensp;&ensp;Prérequis :
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;- Installer [Python 3.11](https://www.python.org/downloads/) 
  
## &ensp;&ensp;&ensp;Installation :
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;- Télécharger le projet depuis [GitHub](https://github.com/CharkaouiSalwa/openclassroom_projet2)

&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;- Ouvrir le terminal

&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;- Se positionner dans le dossier git téléchargé

&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;- Créer un environnement virtuel :
```
python -m venv env
```
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;- Activer l'environnement virtuel : 
```
source  env/bin/activate
```
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;- Installer les bibliothéques nécessaires depuis le fichier requirements.txt :
``` shell
pip install -r requirements.txt
```


## &ensp;&ensp;&ensp;Exécution du projet :

&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;- Pour scrapper un livre : 
```
python scrap_one_book.py
```
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;- Pour scrapper une catégorie : 
```
python scrap_one_category.py
```
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;- Pour scrapper toutes les catégories : 
```
python scrap_all_categories.py
```


## &ensp;&ensp;&ensp;Résultats :
  * Dossier csv contient le résultat d'exécution d'un seul livre, d'une catégorie et toutes les catégories
  * Dossier images contient les images des livres de chaque catégorie
## &ensp;&ensp;&ensp;Contenu du repository GitHub: 
* Fichier scrap_one_book.py
* Fichier scrap_one_category.py
* Fichier scrap_all_categories.py
* Fichier requirements.txt
* Fichier README.md
* Fichier .gitignore

<br/><br/><br/>
*Par Salwa CHARKAOUI*




 



