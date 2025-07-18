from db_connection import get_connection

def actualizar_imagen_usuario(id_usuario, nueva_imagen):
    conn = get_connection
    if conn is None:
        return "Error al tratar de conectar a la base de datos."
    
    with open(nueva_imagen, 'rb') as file:
        imagen_binaria = file.read()

    try:
        cursor = conn.cursor()
        cursor.execute("""
                       UPDATE Usuarios
                       set imagen = ?
                       Where IdUsuario = ?
                       """, (imagen_binaria, id_usuario))
        conn.commit()
        print("Imagen de usuario actualizada exitosamente.")
    except Exception as e:
        print("Error al actualizar la imagen del usuario:", e)
    finally:
        conn.close()
        print("Conexión a la base de datos cerrada.")