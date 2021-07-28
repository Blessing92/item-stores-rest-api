import os
import re

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from db import db

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemsList
from resources.store import Store, StoreList

app = Flask(__name__)

app.config['SQLACHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI', 'sqlite:///data.db')
app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'munga'
api = Api(app)


jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(ItemsList, '/items')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')


if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
