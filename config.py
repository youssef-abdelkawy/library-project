class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://admin:admin@db:5432/librarydb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'secret_key_here'
