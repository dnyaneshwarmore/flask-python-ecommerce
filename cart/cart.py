import json 
import http
from flask import request, make_response
from flask_restful import Resource


class CART(Resource):
    def get(self, user_email):
        # return make_response(json.dumps({'fuck':'the world'}), http.HTTPStatus.Ok)
        return {"fuck":"the world"}

    