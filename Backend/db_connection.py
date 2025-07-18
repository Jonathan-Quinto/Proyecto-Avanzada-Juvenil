import pyodbc

def get_connection():
    try:
        conn = pyodbc.connect(
            'Driver={ODBC Driver 17 for SQL Server};'
            'Server=localhost;'
            'Database=IglesiaDB;'
            'Trusted_Connection=yes;'
        )
        return conn
    except pyodbc.Error as e:
        print("Error al conecta con la base de datos:", e)
        return None