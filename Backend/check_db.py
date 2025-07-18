from db_connection import get_connection

def verificar_usuarios():
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nombre, correo, fecha_registro FROM Usuarios")
            print("\nUsuarios registrados:")
            for usuario in cursor.fetchall():
                print(f"ID: {usuario[0]}, Nombre: {usuario[1]}, Email: {usuario[2]}, Fecha: {usuario[3]}")
        except Exception as e:
            print(f"Error al consultar usuarios: {str(e)}")
        finally:
            conn.close()
    else:
        print("No se pudo conectar a la base de datos")

if __name__ == "__main__":
    verificar_usuarios()