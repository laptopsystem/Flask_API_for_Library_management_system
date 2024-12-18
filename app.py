from flask import Flask, jsonify, request, abort
from models import db, Book, Member  # Ensure correct import of db and models
from config import Config
import hashlib
import time
import functools

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# In-memory token store (for simplicity)
VALID_TOKENS = {}


# Utility function to generate a token for a user (simple)
def generate_token(username):
    timestamp = str(int(time.time()))
    token = hashlib.sha256((username + timestamp + app.config['SECRET_KEY']).encode()).hexdigest()
    VALID_TOKENS[token] = username
    return token


# Token verification decorator
def token_required(f):
    @functools.wraps(f)  # Ensure that the wrapped function retains its original name and signature
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token or token not in VALID_TOKENS:
            abort(401, description="Unauthorized: Invalid or missing token")
        return f(*args, **kwargs)  # Pass arguments to the original function

    return wrapper


# Root route
@app.route('/')
def index():
    return jsonify({"message": "Welcome to the Library Management System API"})


# Search and Pagination for Books
@app.route('/books', methods=['GET'])
def get_books():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    search_title = request.args.get('title', '')
    search_author = request.args.get('author', '')

    query = Book.query

    # Apply search filter
    if search_title:
        query = query.filter(Book.title.ilike(f'%{search_title}%'))
    if search_author:
        query = query.filter(Book.author.ilike(f'%{search_author}%'))

    # Apply pagination
    books = query.paginate(page, per_page, False)

    return jsonify({
        'books': [{'id': book.id, 'title': book.title, 'author': book.author, 'isbn': book.isbn} for book in
                  books.items],
        'total': books.total,
        'page': books.page,
        'per_page': books.per_page
    })


# Add new book (requires token)
@app.route('/book', methods=['POST'])
@token_required
def add_book():
    data = request.get_json()
    new_book = Book(title=data['title'], author=data['author'], isbn=data['isbn'])
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'message': 'Book added successfully'}), 201


# Update book (requires token)
@app.route('/book/<int:id>', methods=['PUT'])
@token_required
def update_book(id):
    data = request.get_json()

    # Check if the book exists
    book = Book.query.get_or_404(id)  # If not found, Flask will automatically send a 404 response

    # Update book details
    book.title = data.get('title', book.title)  # Use existing value if no new data
    book.author = data.get('author', book.author)
    book.isbn = data.get('isbn', book.isbn)

    db.session.commit()  # Commit the changes to the database

    return jsonify({'message': 'Book updated successfully'})


# Delete book (requires token)
@app.route('/book/<int:id>', methods=['DELETE'])
@token_required
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted successfully'})


# User Login to get a token
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Hardcoded user authentication (for demo purposes)
    if username == 'admin' and password == 'password':
        token = generate_token(username)
        return jsonify({'token': token})
    else:
        return jsonify({'message': 'Invalid credentials'}), 401


# CRUD operations for Members (no token required)
@app.route('/members', methods=['GET'])
def get_members():
    members = Member.query.all()
    return jsonify([{'id': member.id, 'name': member.name, 'email': member.email} for member in members])


@app.route('/member', methods=['POST'])
def add_member():
    data = request.get_json()
    new_member = Member(name=data['name'], email=data['email'])
    db.session.add(new_member)
    db.session.commit()
    return jsonify({'message': 'Member added successfully'}), 201


@app.route('/member/<int:id>', methods=['PUT'])
def update_member(id):
    data = request.get_json()
    member = Member.query.get_or_404(id)
    member.name = data['name']
    member.email = data['email']
    db.session.commit()
    return jsonify({'message': 'Member updated successfully'})


@app.route('/member/<int:id>', methods=['DELETE'])
def delete_member(id):
    member = Member.query.get_or_404(id)
    db.session.delete(member)
    db.session.commit()
    return jsonify({'message': 'Member deleted successfully'})


if __name__ == '__main__':
    app.run(debug=True)
