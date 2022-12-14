import mysql.connector

database = mysql.connector.connect(
    host = "localhost",
    user =  "root",
    passwd = "",
    database = "datapy"
)

cursor = database.cursor()

createTable = "create table teste( nome varchar(255), idade int(2));"

cursor.execute(createTable)

database.close()
