'''
all application endpoints are defined here
'''
from flask import request
from flask_restful import Api, Resource

from models import db, User, Book

api = Api()

class Register(Resource):
    def post(self):
        data = request.get_json()
        print(f"Received registration data: {data}")
        if not data or 'username' not in data or 'email' not in data or 'password' not in data:
            return {'message': 'Please provide all required fields'}, 400
        if not all([data['username'], data['email'], data['password']]):
            return {'message': 'Please provide all required fields with data'}, 400
        is_user_exists = User.query.filter((User.username == data['username']) | (User.email == data['email'])).first()
        if is_user_exists:
            return {'message': 'User with this username or email already exists'}, 400
        new_user = User(username=data['username'], email=data['email'], password=data['password'])
        db.session.add(new_user)
        db.session.commit()
        return {'message': 'User registered successfully', 'user': {'username': new_user.username, 'email': new_user.email, 'role': new_user.role}}, 201
api.add_resource(Register, '/register')

class Login(Resource):
    def post(self):
        data = request.get_json()
        print(f"Received login data: {data}")
        if not data or 'email' not in data or 'password' not in data:
            return {'message': 'Please provide all required fields'}, 400
        if not all([data['email'], data['password']]):
            return {'message': 'Please provide all required fields with data'}, 400
        user = User.query.filter_by(email=data['email']).first()
        if user and user.password == data['password']:
            return {'message': 'Login successful', 'user': {'username': user.username, 'email': user.email, 'role': user.role}}, 200
        return {'message': 'Invalid credentials'}, 401
api.add_resource(Login, '/login')

class BookResource(Resource):
    def get(self, book_id=None):
        if book_id is None:
            books = Book.query.all()
            books_list = [{'id': book.id, 'title': book.title, 'description': book.description} for book in books]
            return {'books': books_list}, 200
        else:
            book = Book.query.get(book_id)
            if not book:
                return {'message': 'Book not found'}, 404
            return {'book': {'id': book.id, 'title': book.title, 'description': book.description}}, 200
    def post(self):
        return {'message': 'Create book endpoint'}
    def put(self):
        return {'message': 'Update book endpoint'}
    def delete(self):
        return {'message': 'Delete book endpoint'}
api.add_resource(BookResource, '/books', '/books/<int:book_id>')

print(__name__, 'test the import')