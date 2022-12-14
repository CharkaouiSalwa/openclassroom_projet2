import requests
from bs4 import BeautifulSoup
import csv


from script1 import get_one_book

#fonction qui retourne les informations d'un livre donnée en parametre par catégorie
def get_books_category(nom_categorie,num):
 #pour convertit le numero entier en string
     if isinstance(num, int):
        num = str(num)

     nom_num = nom_categorie+"_"+num
     liste_livre = []
     url = f"https://books.toscrape.com/catalogue/category/books/{nom_num}/index.html"
     r = requests.get(url)
     if r.status_code != 200:
         # pour retourner un message d'erreur si le nom ou num de livre n'existe pas pour pas planter l'apps
         return ["Ce livre n'existe pas, veuillez réessayer"]
     soup = BeautifulSoup(r.content, "html.parser")
     liste = soup.find('ol')
     livres = liste.find_all('article', class_='product_pod')
     for livre in livres:
          link = livre.find('a')['href']
          link = link.split('/')
          link = link[3]
          link = link.split('_')
          if link == "":
              return ["Ce livre n'existe pas, veuillez réessayer"]
          else:
              book_name = link[0]
              book_num = link[1]
              liste_livre.append(get_one_book(book_name,book_num))


     return liste_livre


books_category = get_books_category("travel","2")
print('ok')