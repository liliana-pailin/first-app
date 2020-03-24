from flask import Flask
from flask_restx import Resource, Api
import random

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

@api.route('/I-love-my-dad')
class HelloWorld(Resource):
    def get(self):
        return 'my dad is the best dad ever'
    
    
@api.route('/give-me-an-answer')
class HelloWorld(Resource):
    def get(self):
        anwserList = ['yes','no']
        return random.choice(anwserList))    
        

if __name__ == '__main__':
    app.run(debug=True)
