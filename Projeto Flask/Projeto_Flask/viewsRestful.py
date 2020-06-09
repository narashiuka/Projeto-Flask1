
import json
from datetime import datetime
from flask import render_template, Flask, jsonify, request
from Projeto_Flask import app, api
from flask_restful import Resource, Api
from Projeto_Flask.funhabilidade import Habilidade, Adicionar_habilidade

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
class Desenvolvedor(Resource):
        def get(self, id):
            try:
                response = desenvolvedores[id]
                print(response)
            except IndexError:
                mensagem = f'Registro {id} não existe'
                response = {'status':'Falha', 'mensagem':mensagem}
            except Exception:
                mensagem = 'Erro Descconhecido, procure o administrador da API'
                response = {'status':'Erro', 'mensagem':mensagem}
            return response


        def put(self, id):
            dados = json.loads(request.data)
            desenvolvedores[id] = dados
            return dados


        def delete(self, id):
            desenvolvedores.pop(id)
            return {'status':'Sucesso', 'mensagem':'Registro excluído com sucesso'}

#Lista de todos desenvolvedores e permite incluir um novo desenvolvedor
class Lista_desenvolvedores(Resource):
        def post(self):
            dados = json.loads(request.data)
            posicao = len(desenvolvedores)
            dados['id'] = posicao
            desenvolvedores.append(dados)
            return desenvolvedores[posicao]

        def get(self):
            return desenvolvedores

api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(Lista_desenvolvedores, '/dev/')
api.add_resource(Adicionar_habilidade, '/habilidades/')
api.add_resource(Habilidade, '/habilidades/<int:id>/')
