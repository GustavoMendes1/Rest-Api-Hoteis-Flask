from flask_restful import Resource, Api, reqparse
from models.UserModel import UserModel

class UserResource(Resource):
    
    def get(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            return user.json()
        return{'message': 'User not found.'},404

    def delete(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            try:
                user.delete_user()
            except:
                return{'message': "An internal erro ocurred trying to delete user"},500
            return {'message':'user deleted'}
        return {'message':'user not found'},404



    