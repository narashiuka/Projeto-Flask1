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
    pesoy = {'id':1, 'nome':'Gabriel Roberto', 'profissao':'Engenheiro', 'idade':23, 'jogopreferido':'Minecraft'}
    return jsonify(pesoy)

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

desenvolvedores = [
    {'id':0,
     'nome':'Igor',
     'habilidade':['Python', 'R']},
    {'id':1,
     'nome':'Gabriel',
     'habilidade':['Python', 'Javascript', 'Java']},
    {'id':2,
     'nome':'Pablo',
     'habilidade':['R', 'HTML', 'CSS']}
    ]

#Devolve um desenvolvedor pelo ID, também consegue modificar os dados dos desenvolvedores
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):

    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
            print(response)
        except IndexError:
            mensagem = f'Registro {id} não existe'
            response = {'status':'Falha', 'mensagem':mensagem}
        except Exception:
            mensagem = 'Erro Descconhecido, procure o administrador da API'
            response = {'status':'Erro', 'mensagem':mensagem}
        return jsonify(response)

    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)

    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status':'Sucesso', 'mensagem':'Registro excluído com sucesso'})


#Lista de todos desenvolvedores e permite incluir um novo desenvolvedor
@app.route('/dev/', methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method == 'GET':
         return jsonify(desenvolvedores)


tarefas = [
    {'id':0,
     'responsavel':'Stefani',
     'tarefa':['Limpar', 'Dobrar'],
     'status':'Em Progresso'},
    {'id':1,
     'responsavel':'Gabriel',
     'tarefa':['Limpar', 'Passar', 'Lavar'],
     'status':'Concluida'},
    {'id':2,
     'responsavel':'Henrique',
     'tarefa':['Dobrar', 'Escovar', 'CSS'],
     'status':'Em Progresso'},
    ]
        

     #Devolve um desenvolvedor pelo ID, também consegue modificar os dados dos desenvolvedores
@app.route('/tarefa/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def tarefa(id):

    if request.method == 'GET':
        try:
            response = tarefas[id]
            print(response)
        except IndexError:
            mensagem = f'Registro {id} não existe'
            response = {'status':'Falha', 'mensagem':mensagem}
        except Exception:
            mensagem = 'Erro Descconhecido, procure o administrador da API'
            response = {'status':'Erro', 'mensagem':mensagem}
        return jsonify(response)

    #Altera somente o registro status, e não deixa alterar os outros!
    elif request.method == 'PUT':
        dadosAnteriores = tarefas[id]
        print(dadosAnteriores)
        dados = json.loads(request.data)
        if (dadosAnteriores['responsavel'] != dados['responsavel'] or dadosAnteriores['id'] != dados['id'] or dadosAnteriores['tarefa'] != dados['tarefa']):
            return jsonify({'status':'Erro', 'mensagem':'Somente é possível alterar o registro status'})
        else:
            tarefas[id] = dados
            return jsonify(dados)

    elif request.method == 'DELETE':
        tarefas.pop(id)
        return jsonify({'status':'Sucesso', 'mensagem':'Registro excluído com sucesso'})


#Lista de todos desenvolvedores e permite incluir um novo desenvolvedor
@app.route('/tarefa/', methods=['POST', 'GET'])
def lista_tarefas():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(tarefas)
        dados['id'] = posicao
        tarefas.append(dados)
        return jsonify(tarefas[posicao])
    elif request.method == 'GET':
         return jsonify(tarefas)

