import requests
import mysql.connector
# import isbnlib
# from isbnlib.registry import bibformatters
# from isbnlib import meta
import json
import os, ssl

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="googleDock"
)
mycursor = mydb.cursor()


if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

try:
    with open('inventaire.csv', 'r+') as file:
        for ligne in file:
            ISBN = ligne.rstrip()

            #Google Books
            query = 'isbn:'+ISBN
            params = {"q": query}
            url = r'https://www.googleapis.com/books/v1/volumes'
            response = requests.get(url, params=params)
            jsonResponse = response.json()
            textResponse = response.text
            print(jsonResponse)
            if "items" in jsonResponse:
                for items in jsonResponse['items']:
                    if "title" in items['volumeInfo']:
                        print(items['volumeInfo']['title'])
                        title = items['volumeInfo']['title']
                    if "authors" in items['volumeInfo']:
                        print(items['volumeInfo']['authors'])
                        authors = items['volumeInfo']['authors']
                    if "publishedDate" in items['volumeInfo']:
                        print(items['volumeInfo']['publishedDate'])
                        publishedDate = items['volumeInfo']['publishedDate']
                    if "infoLink" in items['volumeInfo']:
                        print(items['volumeInfo']['infoLink'])
                        infoLink = items['volumeInfo']['infoLink']
                    if "previewLink" in items['volumeInfo']:
                        print(items['volumeInfo']['previewLink'])
                        previewLink = items['volumeInfo']['previewLink']
                    book = {"title": title, "publishedDate": publishedDate, 'authors': '', 'infoLink':infoLink, 'previewLink':previewLink}

                    #sql = "INSERT INTO infolivre (title, publishedDate, authors, language, infoLink, previewLink) VALUES (%s, %s, %s, %s, %s, %s)"
                    #sql = "INSERT INTO infolivre (title, publishedDate, authors, language, infoLink, previewLink) VALUES (%s, %s, %s, %s, %s, %s)"
                    #val = (title,authors,publishedDate,language,infoLink,previewLink)
                    #mycursor.execute(sql, val)
                    mycursor.execute("""INSERT INTO infolivre (title, publishedDate, authors, infoLink, previewLink) VALUES(%(title)s,%(publishedDate)s,%(authors)s,%(infoLink)s,%(previewLink)s)""",book)

                    mydb.commit()

                    print(mycursor.rowcount,"Enregistrement importés.")
                    #cursor.execute("""INSERT INTO infolivre (title,authors,publishedDate,language,infoLink,previewLink) VALUES(%(title)s,%(authors)s,%(publishedDate)s,%(language)s,%(infoLink)s,%(previewLink)s)""")

except FileNotFoundError:
    print("Fichier introuvable")
except IOError:
    print("erreur d’ouverture")
