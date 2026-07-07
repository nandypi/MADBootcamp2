'''
all application endpoints are defined here
'''
from flask import request
from flask_restful import Api, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from flask_caching import Cache

cache = Cache()

from models import db, User, Book

api = Api()

import time

class TestCaching(Resource):
    @cache.cached(timeout=60)
    def get(self):
        user_count = User.query.count(); time.sleep(5)
        return {'message': 'This is response from api'}, 200
api.add_resource(TestCaching, '/test-caching')

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
            access_token = create_access_token(identity=user.email)
            return {'message': 'Login successful', 'user': {'username': user.username, 'email': user.email, 'role': user.role}, 'access_token': access_token}, 200
        return {'message': 'Invalid credentials'}, 401
api.add_resource(Login, '/login')


def is_admin(user_email):
    user = User.query.filter_by(email=user_email).first()
    if user and user.role == 'admin':
        return True
    return False

class BookResource(Resource):
    @jwt_required()
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
    @jwt_required()
    def post(self):
        if not is_admin(get_jwt_identity()):
            return {'message': 'Admin privileges required to create a book'}, 403
        data = request.get_json()
        if not data or 'title' not in data or 'description' not in data:
            return {'message': 'Please provide all required fields'}, 400
        if not all([data['title'], data['description']]):
            return {'message': 'Please provide all required fields with data'}, 400
        book = Book(title=data['title'], description=data['description'])
        db.session.add(book)
        db.session.commit()
        return {'message': 'Book created successfully', 'book': {'id': book.id, 'title': book.title, 'description': book.description}}, 201
    @jwt_required()
    def put(self, book_id):
        if not is_admin(get_jwt_identity()):
            return {'message': 'Admin privileges required to create a book'}, 403
        book = Book.query.get(book_id)
        if not book:
            return {'message': 'Book not found'}, 404
        data = request.get_json()
        if not data:
            return {'message': 'Please provide data to update'}, 400
        book.title = data.get('title', book.title)
        book.description = data.get('description', book.description)
        db.session.commit()
        return {'message': 'Book updated successfully'}
    @jwt_required()
    def delete(self, book_id):
        if not is_admin(get_jwt_identity()):
            return {'message': 'Admin privileges required to delete a book'}, 403
        book = Book.query.get(book_id)
        if not book:
            return {'message': 'Book not found'}, 404
        db.session.delete(book)
        db.session.commit()
        return {'message': 'Book deleted successfully'}
api.add_resource(BookResource, '/books', '/books/<int:book_id>')

print(__name__, 'test the import')