from flask import Flask, jsonify
from flask_restful import Resource, Api
from resources.hotel import Hoteis,Hotel
from resources.UserResource import UserResource,UserRegister,UserLogin, UserLogout
from flask_jwt_extended import JWTManager
from blacklist import BLACKLIST

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///BANCO.DB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'DontTellAnymore'
app.config['JWT_BLACKLIST_ENABLED'] = True
api = Api(app)
jwt = JWTManager(app)

@app.before_first_request
def cria_banco():
    banco.create_all()

@jwt.token_in_blacklist_loader
def verifica_blacklist(token):
    return token['jti'] in BLACKLIST

@jwt.revoked_token_loader
def token_de_acesso_invalido():
    return jsonify({'message':'You have been logged out.'}),401

api.add_resource(Hoteis,'/hoteis')
api.add_resource(Hotel,'/hoteis/<string:hotel_id>')
api.add_resource(UserResource,'/usuarios/<string:user_id>')
api.add_resource(UserRegister,'/cadastro')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')


if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True)

