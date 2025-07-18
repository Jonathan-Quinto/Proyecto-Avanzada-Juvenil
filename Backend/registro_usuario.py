from db_connection import get_connection

def registrar_usuario(nombre, correo, contraseña, imagen_path):
    conn = get_connection()
    if conn is None:
        return "Error al tratar de conectar a la base de datos."
    
    with open(imagen_path, 'rb') as file:
        imagen_binaria = file.read()

    try:
        cursor = conn.cursor()
        cursor.execute("""
                       Insert Into Usuarios (NombreCompleto, Correo, Contraseña, Imagen)
                          Values (?, ?, ?, ?)
                       """, (nombre, correo, contraseña, imagen_binaria))
        conn.commit()
        print("Usuario registrado exitosamente.")
    except Exception as e:
        print("Error al registrar el usuario:", e)
    finally:
        conn.close()