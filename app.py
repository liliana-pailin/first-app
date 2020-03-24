from flask import Flask
from flask_restx import Resource, Api

app = Flask(__name__)
api = Api(app)

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

@api.route('/test')
class HelloWorld(Resource):
    def get(self):
        return "I'm here"   
    
if __name__ == '__main__':
    app.run(debug=True)
