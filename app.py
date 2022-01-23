from flask import Flask, send_from_directory
from flask_restful import Api, Resource, reqparse
# import flask_cors
from flask_cors import CORS #comment this on deployment
from api.BasicHandler import BasicHandler
from api.FormHandler import FormHandler

app = Flask(__name__, static_url_path='', static_folder='frontend/src')
CORS(app)
api = Api(app)

@app.route("/", defaults={'path':''})
def serve(path):
    return send_from_directory(app.static_folder,'index.js')

api.add_resource(BasicHandler, '/flask/hello')
api.add_resource(FormHandler, '/flask/submitForm')

