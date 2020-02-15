

import json 
import http
from flask import request, make_response, session
from flask_restful import Resource
import sys
sys.path.append("..")
from models import User, Product, Cart, db



class PRODUCTCATEGORY(Resource):

    def get(self, prod_category):
        user_email = request.headers.get("user_email")
        if (not self.doesUserexists(user_email)):
                return {"error": "user does not  exists"}, 404

        if (not self.isAlreadyLoggedIn(user_email)):
            return {"message": "please login "}, 400

        products = Product.query.filter_by(category = prod_category).all()
        response = []
        for product in products:
             prod = {}
             prod["name"] = product.name
             prod["category"] = product.category
             prod["price"] = product.price
             response.append(prod)

        return response, 200

    def doesUserexists(self,useremail):
        user = User.query.filter_by(user_email=useremail).first()
        if (user):
            return True
        else:
            return False

    def isAlreadyLoggedIn(self, useremail):   
        if session.get(useremail, None): 
                print("user Already logged in",useremail)
                return True
        return False



class PRODUCT(Resource):
    
    def get(self):
        user_email = request.headers.get("user_email")
        if (not self.doesUserexists(user_email)):
                return {"error": "user does not  exists"}, 404

        if (not self.isAlreadyLoggedIn(user_email)):
            return {"message": "please login "}, 400

        products = Product.query.all()
        response = []
        for product in products:
             prod = {}
             prod["name"] = product.name
             prod["category"] = product.category
             prod["price"] = product.price
             response.append(prod)

        return response, 200

    def post(self):

        user_email = request.headers.get("user_email")
        product_data = json.loads(request.data.decode("utf-8"))
        print(type(product_data))
        print("user email", user_email)
        if (not self.doesUserexists(user_email)):
                return {"error": "user does not  exists"}, 404

        if (not self.isAlreadyLoggedIn(user_email)):
            return {"message": "please login "}, 400
        
        user = User.query.filter_by(user_email=user_email).first()
        
        if "seller" == user.user_type:
            product = Product(name=product_data["name"],category =  product_data["category"], price =product_data["price"])
            db.session.add(product)
            db.session.commit()
            return {"message": "product added successfully"}
            
        return {"message": "user is not authorised to add products"}, 401 
         

    def doesUserexists(self,useremail):
        user = User.query.filter_by(user_email=useremail).first()
        if (user):
            return True
        else:
            return False

    def isAlreadyLoggedIn(self, useremail):   
        if session.get(useremail, None): 
                print("user Already logged in",useremail)
                return True
        return False
