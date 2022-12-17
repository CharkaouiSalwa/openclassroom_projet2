import requests
from bs4 import BeautifulSoup
import csv, os

#function to get one book by parameters (string:book name and string:book number)
# return list of details of the book
def get_one_book(nom_livre,numero):
     try:
        #convert int to string
        if isinstance(numero,int):
            numero = str(numero)

        nom_num = nom_livre+"_"+numero
        liste_livre = []
        url =f"https://books.toscrape.com/catalogue/{nom_num}/index.html"
        r = requests.get(url)
        if r.status_code!=200:
            #return error msg if url doesn't work
            return ["Cette page n'existe pas, veuillez réessayer"]
        soup = BeautifulSoup(r.content, "html.parser")
        product_url =url

        image = soup.find('img')
        image_url = image.attrs['src']
        titre = image.attrs['alt']
        product_description=soup.findAll('p')[3].text
        category =soup.findAll('a')[3].text
        table = soup.findAll('table')[0]
        rows = table.findAll('tr')
        upc = table.findAll('td')[0].text
        product_type=table.findAll('td')[1].text
        price_excl_tax = table.findAll('td')[2].text
        price_incl_tax = table.findAll('td')[3].text
        tax =table.findAll('td')[4].text
        number_available= table.findAll('td')[5].text
        reviews_rating = soup.find('p',class_='star-rating')
        reviews_rating = reviews_rating['class'][1]
        liste_livre.append([product_url,upc,titre,price_incl_tax,price_excl_tax,number_available,product_description,category,reviews_rating,image_url])
        return liste_livre
     except Exception as e:
             return [e]
#run function get_one_book
one_book = get_one_book("a-light-in-the-attic",1000)

#create a ccv file
def create_csv():
 try:
     en_tete = ["product_url","upc","titre","price_incl_tax","price_excl_tax","number_available","product_description","category","reviews_rating","image_url"]
     fichier = "one_book.csv"
     # checking if the directory csv exist or not.
     if not os.path.exists("csv"):
         # if the csv directory is not present then create it.
         os.makedirs("csv")
     with open(f'csv/{fichier}', 'w') as csv_file:
      writer = csv.writer(csv_file, delimiter=',')
      writer.writerow(en_tete)
      writer.writerows(one_book)
 except Exception as e:
     print(e)

#run function create_csv
create_csv()