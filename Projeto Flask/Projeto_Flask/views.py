"""
Routes and views for the flask application.
"""

import json
from datetime import datetime
from flask import render_template, Flask, jsonify, request
from Projeto_Flask import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/pessoa')
def pessoa():
    pesoy = jsonify({'id':1, 'nome':'Gabriel Roberto', 'profissao':'Engenheiro', 'idade':23, 'jogopreferido':'Minecraft'})
    return render_template(pesoy.nome)

#@app.route('/soma/<int:a>/<int:b>')
#def somando(a, b):
#    soma = int(a) + int(b)
#    return jsonify({'Soma':soma})

@app.route('/soma', methods=['POST', 'GET'])
def somando():
    if (request.method == 'POST'):
        dados = json.loads(request.data)
        total = sum(dados['valores'])
    elif (request.method == 'GET'):
        total = 10 + 10
    return jsonify({'soma':total})