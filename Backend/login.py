from db_connection import get_connection

def login_usuario(correo, contraseña):
    conn = get_connection()
    if not conn:
        return False
    
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT IdUsuario FROM usuarios 
            WHERE correo = ? AND contraseña = ?
        """, (correo, contraseña))
        return cursor.fetchone() is not None
    except Exception as e:
        print("Error al iniciar sesión:", e)
        return False
    finally:
        conn.close()