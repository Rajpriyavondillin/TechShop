import mysql.connector
from mysql.connector import Error
from util.DBPropertyUtil import DBPropertyUtil

def get_connection():
    try:
        props = DBPropertyUtil.get_db_properties()
        return mysql.connector.connect(
            host=props["host"],
            user=props["user"],
            password=props["password"],
            database=props["database"]
        )
    except Error as e:
        print("Database connection failed:", e)
        return None
