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

if __name__== '__main__':
    app.run(debug=True, port=5000)