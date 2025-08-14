# Install MySQL on your computer
# https://dev.mysql.com/downloads/installer/
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python


# import mysql.connector
import pymysql

database = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password123!',
)

# prepare a cursor object
cursorObject = database.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE elderco")

print("Database Setup ALL Done!")

