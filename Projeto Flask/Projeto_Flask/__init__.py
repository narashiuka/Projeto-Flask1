"""
The flask application package.
"""

from flask import Flask, jsonify
app = Flask(__name__)

import Projeto_Flask.views
