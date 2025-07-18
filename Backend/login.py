from db_connection import get_connection

def login_usuario (correo, contraseña):
    conn = get_connection()
    if not conn:
        return "Error al tratar de conectar a la base de datos."
    

    try:
        cursor = conn.cursor()
        cursor.execute("""
                       Select IdUsuario from usuarios
                       Where correo = ? and contraseña = ?
                       """, (correo, contraseña))
        
        resultado = cursor.fetchone()
        return resultado is not None
    except Exception as e:
        print("Error al iniciar sesión:", e)
        return False
    finally:
        conn.close()
        print("Conexión a la base de datos cerrada.")