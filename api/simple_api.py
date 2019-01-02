from flask import Flask
#Resource - allows you to create a resource to connect to using the REST API
#API - is a wrapper around the entire application, that allows the resource to connect
from flask_restful import Resource, Api


app = Flask(__name__)


api = Api(app)


#CREATE A RESOURCE => create a class

class HelloWorld(Resource):

    def get(self):
        return {'hello':'world'}

#CONNECT THE RESOURCE
#pass in the class and the url you want to connect it to
api.add_resource(HelloWorld,'/')

if __name__ == '__main__':
    app.run(debug=True)
