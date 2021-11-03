import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="googleDock"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE infolivre (title VARCHAR(255),publishedDate VARCHAR(255),authors VARCHAR(255),language VARCHAR(255),infoLink VARCHAR(255),previewLink VARCHAR(255))")
