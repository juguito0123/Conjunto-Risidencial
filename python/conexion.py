import psycopg2

# Parámetros de la conexión a la base de datos
db_params = {
    'dbname': 'Residencia',
    'user': 'julian',
    'password': '123',
    'host': 'localhost',  # O la dirección IP de tu servidor PostgreSQL
    'port': '5432'  # El puerto predeterminado de PostgreSQL es 5432
}

try:
    # Conectar a la base de datos
    conn = psycopg2.connect(**db_params)

    # Crear un cursor
    cursor = conn.cursor()

    # Realizar operaciones en la base de datos
    cursor.execute("SELECT * FROM Prueba")
    data = cursor.fetchall()
    for row in data:
        print(row)

    # Cerrar el cursor y la conexión
    cursor.close()
    conn.close()

except (Exception, psycopg2.Error) as error:
    print("Error al conectar a la base de datos:", error)