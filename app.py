from flask import Flask, render_template, request
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)

@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def hello():
    if request.method == 'GET':
        # get data
        return {"message": "Get method request received"}
    elif request.method == 'POST':
        # create item with data
        return {"message": "POST request received"}
    elif request.method == 'PUT':
        # update item with data
        return {"message": "PUT request received"}
    elif request.method == 'DELETE':
        # delete item with id
        return {"message": "DELETE request received"}
    return render_template('index.html')

class HelloWorld(Resource):
    def get(self):
        return {'message': 'Hello, World!'}
    def post(self):
        return {'message': 'POST request received'}
    def put(self):
        return {'message': 'PUT request received'}
    def delete(self):
        return {'message': 'DELETE request received'}
    
class Students(Resource):
    def get(self):
        # students = Students.query.all()
        # students = [student.name for student in students]
        students = ['Alice', 'Bob', 'Charlie']
        return {'students': students}

api.add_resource(HelloWorld, '/hello')
api.add_resource(Students, '/students')

if __name__ == '__main__':
    app.run(debug=True)