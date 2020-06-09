from flask_restful import Resource
from Projeto_Flask import app, api
from flask import render_template, Flask, jsonify, request
import json

lista_habilidades = ['Python', 'DBA', 'Javascript', 'Java', 'C#', 'C++']

class Habilidade(Resource):
        def get(self):
            return lista_habilidades

        def put(self, id):
            dados = json.loads(request.data)
            lista_habilidades[id] = dados
            return dados

        def delete(self, id):
            lista_habilidades.pop(id)
            return {'status':'Sucesso', 'mensagem':'Registro excluído com sucesso'}

class Adicionar_habilidade(Resource):
        def post(self):
            dados = json.loads(request.data)
            posicao = len(lista_habilidades)
            dados['id'] = posicao
            desenvolvedores.append(dados)
            return lista_habilidades[posicao]

        def get(self):
            return lista_habilidades