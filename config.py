# config.py

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///library.db'  # SQLite for simplicity
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your_secret_key_here'  # Secret key for token generation
