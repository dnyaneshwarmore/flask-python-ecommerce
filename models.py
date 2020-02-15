from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
app = Flask(__name__)

# give mysql db url with proper username, password and database name 

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://junaid:khan@localhost/karza'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
api = Api(app)

#Database models for User, Product details and cart details

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    user_email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120),nullable=False)
    user_type = db.Column(db.String(120),nullable=False)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    category = db.Column(db.String(80),nullable=False)
    price = db.Column(db.Integer, nullable=False)

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(80), unique=True, nullable=False)
    category = db.Column(db.String(80),nullable=False)