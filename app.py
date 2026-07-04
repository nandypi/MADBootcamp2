from flask import Flask, render_template, request
from flask_jwt_extended import JWTManager


app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your-secret-key'  # Change this to a random secret key
jwt = JWTManager(app)

# connect with the api endpoints defined in apis.py
from apis import api, Resource
api.init_app(app)

# connect with database models defined in models.py
from models import db, User
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

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
api.add_resource(HelloWorld, '/hello')

if __name__ == '__main__':

    with app.app_context():
        
        db.create_all()  # Create database tables if they don't exist

        admin = User.query.filter_by(role='admin').first()
        
        if admin:
            print("Admin user already exists.")
        else:
            print("Admin user does not exist. Creating admin user...")
            admin = User(username='admin', email='admin@gmail.com', role='admin', password='admin')
            db.session.add(admin)
            db.session.commit()

    app.run(debug=True)