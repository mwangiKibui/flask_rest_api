from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

#Init app
app = Flask(__name__)
app.config.from_pyfile('config.py')
#Init db
db = SQLAlchemy(app)
#Init Ma
ma = Marshmallow(app)
from routes import *
#Run server
if __name__ == '__main__':
    app.run()
