import requests
from bs4 import BeautifulSoup
import csv,os

from script2 import get_books_category

#function to get  all books of each category by parameters
#return list of details of the books of all each category
def get_all_books_each_category():
    try:
        liste_livre = []
        url = "http://books.toscrape.com/"
        r = requests.get(url)
        if r.status_code != 200:
            #return error msg if name or number book is not exist
            return ["Cette page n'existe pas, veuillez réessayer"]
        soup = BeautifulSoup(r.content, "html.parser")
        menu_category = soup.find('ul',class_='nav-list')
        menu_category = menu_category.findAll('li')
        category_href = ""
        category_name = ""
        category_number = ""
        for i in range(1,len(menu_category)):
            category_href = menu_category[i].find('a')['href']
            category_href= category_href.split('/')
            category_href=category_href[3]
            category_href=category_href.split('_')
            category_name=category_href[0]
            category_number=category_href[1]
            liste_livre.append(get_books_category(category_name,category_number))

        #all books in one list
        # all_livre_liste = []
        # for i in range(len(liste_livre)):
        #    all_livre_liste = all_livre_liste + liste_livre[i]

        return liste_livre

    except Exception as e:
      return [e]


#run function get_all_books_each_category
books_each_cat = get_all_books_each_category()

#create csv for each category
def create_csv():
    try:
        en_tete = ["product_url", "upc", "titre", "price_incl_tax", "price_excl_tax", "number_available",
                   "product_description", "category", "reviews_rating", "image_url"]
        category_name = ""
        for i in range(len(books_each_cat)):
            category_name = books_each_cat[i][0][0][7] #to get name of category from list
            category_name = category_name.lower() #convert all char to lower
            fichier = f"{category_name}-category.csv"
            # checking if the directory csv/categories exist or not.
            if not os.path.exists("csv/categories"):
                # if the csv/categories directory is not present then create it.
                os.makedirs("csv/categories")
            with open(f'csv/categories/{fichier}', 'w') as csv_file:
                writer = csv.writer(csv_file, delimiter=',')
                writer.writerow(en_tete)
                writer.writerows(books_each_cat[i])
    except Exception as e:
        return [e]

#run function create_csv()
create_csv()