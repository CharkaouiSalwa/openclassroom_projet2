import requests
from bs4 import BeautifulSoup
import csv,os


from script1 import get_one_book

#function to get  books_category by parameters (string:book name and string:book number)
def get_books_category(nom_categorie,num):
    try:
     #convert int to string
         if isinstance(num, int):
            num = str(num)

         nom_num = nom_categorie+"_"+num
         liste_livre = []
         url = f"https://books.toscrape.com/catalogue/category/books/{nom_num}/index.html"
         r = requests.get(url)
         if r.status_code != 200:
             #return error msg if url doesn't work
             return ["Cette page n'existe pas, veuillez réessayer"]
         soup = BeautifulSoup(r.content, "html.parser")
         liste = soup.find('ol')
         livres = liste.find_all('article', class_='product_pod')
         nombre_page = soup.find('li',class_='current')
         if nombre_page:
             #strip to delete whitespaces in string
             nombre_page = soup.find('li',class_='current').text.strip()
             #split the text from space
             nombre_page = nombre_page.split(' ')
             #convert string to int
             nombre_page = int(nombre_page[3])
         #get all books from page 1 (index)
         for livre in livres:
              link = livre.find('a')['href']
              #split the text from '/'
              link = link.split('/')
              link = link[3]
              link = link.split('_')
              if link == "":
                  return ["Ce livre n'existe pas, veuillez réessayer"]
              else:
                  book_name = link[0]
                  book_num = link[1]
                  liste_livre.append(get_one_book(book_name,book_num))
         #get books from next pages
         if nombre_page:
             for i in range(2,nombre_page+1):
                url = f"https://books.toscrape.com/catalogue/category/books/{nom_num}/page-{i}.html"
                r = requests.get(url)
                if r.status_code != 200:
                    # return error msg if name or number book is not exist
                    return ["Cette page n'existe pas, veuillez réessayer"]
                soup = BeautifulSoup(r.content, "html.parser")
                liste = soup.find('ol')
                livres = liste.find_all('article', class_='product_pod')
                # get all books from other pages
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
                        liste_livre.append(get_one_book(book_name, book_num))
         return liste_livre
    except Exception as e:
      return [e]

#test run of get_books_category
#books_category = get_books_category("mystery","3") #2 pages
books_category = get_books_category("travel","2") #11 books
#books_category = get_books_category("fiction","10") #4 pages


#create a ccv file
def create_csv():
    try:
     en_tete = ["product_url","upc","titre","price_incl_tax","price_excl_tax","number_available","product_description","category","reviews_rating","image_url"]
     fichier = "books_category.csv"
     # checking if the directory csv exist or not.
     if not os.path.exists("csv"):
         # if the csv directory is not present then create it.
         os.makedirs("csv")
     with open(f'csv/{fichier}', 'w') as csv_file:
      writer = csv.writer(csv_file, delimiter=',')
      writer.writerow(en_tete)
      writer.writerows(books_category)
    except Exception as e:
        return [e]

#run function create_csv()
create_csv()

