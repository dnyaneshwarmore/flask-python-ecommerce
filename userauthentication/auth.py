

import json 
import http
from flask import request, make_response, session
from flask_restful import Resource
import sys
sys.path.append("..")
from models import User, db

class LOGIN(Resource):
    def post(self):
        
        user_email = request.headers.get("user_email")
        password = request.headers.get("password")
        print("user email", user_email)
        if (not self.doesUserexists(user_email)):
                return {"error": "user does not  exists"}, 404

        if (self.isAlreadyLoggedIn(user_email)):
            return {"message": "user Already logged in"}, 400
        
        user = User.query.filter_by(user_email=user_email).first()
        
        if password == user.password:
            session[user_email] = user.user_email
            return {"message": "user logged in successfully"}, 200

        return {"message": "wrong credentials"}, 401 
         

    def doesUserexists(self,useremail):
        user = User.query.filter_by(user_email=useremail).first()
        if (user):
            return True
        else:
            return False

    def isAlreadyLoggedIn(self, useremail):
        # user = User.query.filter_by(user_email=useremail).first()
        # print("user", user)
       
        if session.get(useremail, None): 
                print("user Already logged in",useremail)
                return True
        return False

class SIGNUP(Resource):
    def post(self):
        try:
            name = request.headers.get("name")
            user_email = request.headers.get("user_email")
            password = request.headers.get("password")
            user_type = request.headers.get("user_type")
            
            if (self.doesUserexists(user_email)):
                return {"error": "user Already exists"}, 403
            user = User(name = name, user_email=user_email, password=password, user_type=user_type)
            db.session.add(user)
            db.session.commit()
            session[user_email] = user.user_email
            print("login success for user", user)
            return {"message": "successfully created user"}, 200

        except Exception as e:
            print(e)
            return str(e), 403

    def doesUserexists(self,useremail):
        user = User.query.filter_by(user_email=useremail).first()
        if (user):
            return True
        else:
            return False

class LOGOUT(Resource):
    def post(self):
        user_email = request.headers.get("user_email")
        
        if session.get(user_email, None):
            del session[user_email]
            return {"message": "successfully signed Out"}, 200
                
        return {"message": "user already logged Out"}, 400 