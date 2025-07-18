import pyodbc
from db_connection import get_connection

def test_connection():
    print("=== Iniciando prueba de conexión a la base de datos ===")
    
    try:
        # 1. Probar conexión básica
        conn = get_connection()
        if conn:
            print("✓ Conexión establecida correctamente")
            
            # 2. Probar consulta simple
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sys.databases")
            databases = cursor.fetchall()
            
            print("\nBases de datos disponibles:")
            for db in databases:
                print(f"- {db[0]}")
            
            # 3. Probar consulta a tu tabla de usuarios
            try:
                cursor.execute("SELECT TOP 3 NombreCompleto, Correo FROM Usuarios")
                usuarios = cursor.fetchall()
                
                print("\nPrimeros 3 usuarios registrados:")
                for usuario in usuarios:
                    print(f"- Nombre: {usuario[0]}, Email: {usuario[1]}")
            except pyodbc.Error as e:
                print(f"\n⚠ No se pudo acceder a la tabla Usuarios: {e}")
            
            # Cerrar conexión
            conn.close()
            print("\n✓ Conexión cerrada correctamente")
        else:
            print("✗ No se pudo establecer la conexión")
            
    except Exception as e:
        print(f"\n✗ Error durante la prueba: {str(e)}")

if __name__ == "__main__":
    test_connection()