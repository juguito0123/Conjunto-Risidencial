from flask import Flask, render_template, request,url_for, redirect, jsonify
import psycopg2

# Parámetros de conexión
db_params = {
    'dbname': 'Residencia',
    'user': 'julian',
    'password': '123',
    'host': 'localhost',
    'port': '5432'
}

app=Flask(__name__)

@app.route('/')
def index():
    data={
        'titulo': 'Residentes'
    }
    return render_template('index.html',data=data)

@app.route('/Zonas-Comunes')
def Zonas_Comunes():
    data={
        'titulo': 'ZonasComunes'
    }
    return render_template('Zonas_Comunes.html',data=data)

@app.route('/Facturaxion')
def Facturaxion():
    data={
        'titulo': 'Facturaxion'
    }
    return render_template('Facturaxion.html',data=data)

@app.route('/nueva_pagina', methods=['POST'])
def nueva_pagina():
    opcion_seleccionada = request.form.get('opcion')

    data = {
        'titulo': 'Residente'
    }

    if opcion_seleccionada == 'opcion1':
        return render_template('vehiculos.html', data=data)
    elif opcion_seleccionada == 'opcion2':
        return render_template('personas.html', data=data)
    elif opcion_seleccionada == 'opcion3':
        return render_template('inmuebles.html', data=data)
    else:
        # Página predeterminada o manejar otro caso
        return render_template('nueva_pagina_default.html', data=data)
    



@app.route('/procesar_formulario', methods=['POST'])
def procesar_formulario():
    # Obtener los datos del formulario desde la solicitud JSON
    datos_residente = request.json

    # ... (resto del código para insertar en la base de datos)

    # Devolver una respuesta JSON
    return jsonify({"mensaje": "Datos del residente insertados correctamente"})


if __name__== '__main__':
    app.run(debug=True, port=5000)