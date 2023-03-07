import mysql.connector

# connection with mysql
name_database = input('Database name: ')

database = mysql.connector.connect(
    host = "localhost",
    user =  "root",
    passwd = "",
    database = name_database
)

cursor = database.cursor()

# function Create
def CreateTable():
    props_table = []

    # table properties (name, columns quantity) 
    props_table.append(input("Table name: "))
    props_table.append(int(input("Columns quantity: ")))

    createtable = f"CREATE table {props_table[0]}("

    # create the columns
    for column in range (props_table[1]):
        props_column = []

        print('-'*20)

        props_column.append(input(f"{column + 1}° Column name: "))
        props_column.append(input(f"{column + 1}° Column type: "))
        props_column.append(input(f"{column + 1}° Column space: "))

        createtable += f'{props_column[0]} {props_column[1]} ({props_column[2]})'

        if column < props_table[1] - 1:
            createtable += ',' 

    createtable += ");"

    cursor.execute(createtable)

    print("TABLE CREATE SUCESSED!!")

def Select():

    option = int(input(
'''-----------------------
|[ 1 ] - All Table     |
|[ 2 ] - Only columns  | 
-----------------------
Select the option:
'''))
    
    

# database.close()
