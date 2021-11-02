import requests
import isbnlib
from isbnlib.registry import bibformatters
from isbnlib import meta
import json
import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

try:
    with open('inventaire.csv', 'r+') as file:
        for ligne in file:
            ISBN = ligne.rstrip()

            # #Open Library
            # url = "https://openlibrary.org/api/books?bibkeys=ISBN:" + ISBN + "&format=json"
            # payload = {}
            # headers = {}
            # response = requests.request("GET", url, headers=headers, data=payload)
            # print(response.json())

            #Google Books
            query = 'isbn:'+ISBN
            params = {"q": query}
            url = r'https://www.googleapis.com/books/v1/volumes'
            response = requests.get(url, params=params)
            print(response.json())

            # #BNF
            # SERVICE = "bnf"
            # try:
            #     bibtex = bibformatters["json"]
            #     print(json.loads(bibtex(meta(ISBN, SERVICE))))
            #     print(isbnlib.desc(ISBN))
            # except AttributeError:
            #     print("erreur BNF")

except FileNotFoundError:
    print("Fichier introuvable")
except IOError:
    print("erreur d’ouverture")
