from flask import Flask, render_template, request,url_for, redirect, jsonify

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
    
if __name__== '__main__':
    app.run(debug=True, port=5000)