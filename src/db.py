import mysql.connector
#Se necesita usar el comando: pip3 install mysql-connector-python

database = mysql.connector.connect(
    user='root',
    password='federico546',
    host='127.0.0.1',
    database='python_db',
    port = '3306'
)