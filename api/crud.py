from flask import Flask
#Resource - allows you to create a resource to connect to using the REST API
#API - is a wrapper around the entire application, that allows the resource to connect
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)

puppies = []

class PuppyNames(Resource):

    def get(self,name):
        pass

    def post(self,name):
        pup = {'name':name}
        puppies.append(pup)
        return pup

    def delete(self,name):
        pass

api.add_resource(HelloWorld,'/')

if __name__ == '__main__':
    app.run(debug=True)
