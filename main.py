from models import db, app, api
from cart.cart import CART 
from products.products import PRODUCT, PRODUCTCATEGORY
from userauthentication.auth import LOGIN, LOGOUT, SIGNUP


#add all views to api object
api.add_resource(CART, "/cart/<string:user_email>")
api.add_resource(LOGIN, "/login")
api.add_resource(SIGNUP, "/signup")
api.add_resource(LOGOUT, "/logout")
api.add_resource(PRODUCT, "/product")
api.add_resource(PRODUCTCATEGORY, "/product/category/<string:prod_category>")

def main():
    db.create_all()
    #secret key shoould be very strong
    app.secret_key = 'My Secret'
    app.run(debug=True, port=8080)

if __name__ == "__main__":
    main()