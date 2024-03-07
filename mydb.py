import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root',
)


cursorObject = dataBase.cursor()


cursorObject.execute("CREATE DATABASE SHEEEESH_ORG")

print("hello world i am done with you")