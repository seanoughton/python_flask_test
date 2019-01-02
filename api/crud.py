from flask import Flask
#Resource - allows you to create a resource to connect to using the REST API
#API - is a wrapper around the entire application, that allows the resource to connect
from flask_restful import Resource, Api

from secure_check import authenticate,identity
#jwt is the flask version of the api
from flask_jwt import JWT,jwt_required


app = Flask(__name__)
app.config['SECRET_KEY']='mysecretkey'

api = Api(app)
jwt = JWT(app,authenticate,identity)

puppies = []

class PuppyNames(Resource):

    def get(self,name):
        for pup in puppies:
            if pup['name'] == name:
                return pup
        return {'name':None},404 #you can also specify the HTTP Status code

    def post(self,name):
        pup = {'name':name}
        puppies.append(pup)
        return pup

    def delete(self,name):
        for ind,pup in enumerate(puppies):
            if pup['name'] == name:
                deleted_pup = puppies.pop(ind) #pop the puppy at that index
                return {'note':'delete success'}

#this decorator means that if you want to get al the names, then you need to authenticate through jwt
class AllNames(Resource):

    @jwt_required()
    def get(self):
        # return puppies
        return {'puppies':puppies}

api.add_resource(PuppyNames,'/puppy/<string:name>')
api.add_resource(AllNames,'/puppies')



if __name__ == '__main__':
    app.run(debug=True)
