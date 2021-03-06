from db import db
from flask_restful import Resource,reqparse
from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be blank"
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be blank"
                        )
    def post(self):
        
        data=UserRegister.parser.parse_args()

        user=UserModel.find_by_username(data['username'])

        if user:
            return {"message":"User is already registered"},400
        
        #user=UserModel(data['username'],data['password'])
        user=UserModel(**data)
        user.save_to_db()

        return {'message':"User created successfully."},201
    
