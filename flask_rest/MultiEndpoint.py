from flask import Flask
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self, message):
        return {"hello":message}


api.add_resource(HelloWorld, '/hello/<string:message>', '/world/<string:message>')

if __name__ == '__main__':
    app.run(debug = True)
