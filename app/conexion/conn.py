import psycopg2

# Parámetros de conexión
db_params = {
    'dbname': 'Residencia',
    'user': 'julian',
    'password': '123',
    'host': 'localhost',
    'port': '5432'
}

# Intenta establecer la conexión
try:
    # Crear una conexión
    conn = psycopg2.connect(**db_params)

    # Crear un cursor para ejecutar consultas
    cursor = conn.cursor()

    # Ejemplo de consulta
    cursor.execute("SELECT * FROM tu_tabla;")
    rows = cursor.fetchall()

    # Hacer algo con los resultados
    for row in rows:
        print(row)

except psycopg2.Error as e:
    print("Error al conectar a la base de datos:", e)

finally:
    # Cerrar cursor y conexión
    if cursor:
        cursor.close()
    if conn:
        conn.close()
