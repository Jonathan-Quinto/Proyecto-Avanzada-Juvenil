import pyodbc
import os

def get_connection():
    try:
        conn = pyodbc.connect(
            'Driver={ODBC Driver 17 for SQL Server};'
            'Server=Jonathan;'
            'Database=IglesiaDB;'
            'Trusted_Connection=yes;'
        )
        return conn
    except pyodbc.Error as e:
        print("Error al conectar con la base de datos:", e)
        return None