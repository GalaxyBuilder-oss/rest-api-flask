# database.py

import os
from dotenv import load_dotenv, dotenv_values
import mysql.connector
from mysql.connector import Error

load_dotenv()

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST"),
            user=os.getenv("MYSQL_USER"),
            passwd=os.getenv("MYSQL_PASSWORD")
        )
        connection.cursor().execute("Create database if not exists "+ os.getenv("MYSQL_DB"))
        connection = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST"),
            user=os.getenv("MYSQL_USER"),
            passwd=os.getenv("MYSQL_PASSWORD"),
            database=os.getenv("MYSQL_DB")
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

db_connection = create_connection()
