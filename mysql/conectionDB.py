# import mysql.connector

# # create the connection with mysql
# def Connection():
#     database = input('Database name: ')

#     database = mysql.connector.connect(
#         host = "localhost",
#         user =  "root",
#         passwd = "",
#         database = database
#     )

#     cursor = database.cursor()

# # method Create
# def CreateTable():
props_table = []

# table properties (name, columns quantity) 
props_table.append(input("Table name: "))
props_table.append(int(input("Columns quantity: ")))

createtable = f"CREATE table {props_table[0]}("

# create the columns
for column in range (props_table[1]):
    props_column = []

    print('-'*20)

    props_column.append(input(f"{column + 1}° Column name:"))
    props_column.append(input("Column type:"))
    props_column.append(input("Column space:"))

    createtable += f'{props_column[0]} {props_column[1]} ({props_column[2]}),'

createtable += ");"

print(createtable)
# cursor.execute(createTable)

# database.close()
