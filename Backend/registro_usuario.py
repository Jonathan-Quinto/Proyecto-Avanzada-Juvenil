from db_connection import get_connection

def registrar_usuario(nombre, correo, contraseña):
    conn = get_connection()
    if not conn:
        return False
    
    try:
        cursor = conn.cursor()
        # Usamos el procedimiento almacenado
        cursor.execute("EXEC sp_registrar_usuario ?, ?, ?", 
                      (nombre, correo, contraseña))
        conn.commit()
        return True
    except pyodbc.Error as e:
        print(f"Error al registrar usuario: {str(e)}")
        return False
    finally:
        if conn:
            conn.close()