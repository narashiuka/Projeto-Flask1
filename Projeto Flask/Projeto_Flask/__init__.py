"""
The flask application package.
"""

from flask import Flask, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

#import Projeto_Flask.views
import Projeto_Flask.viewsRestful
