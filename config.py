class Config:
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://jokuvaan:12345@localhost:5432/postgres'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = 'ap'
    JWT_ERROR_MESSAGE_KEY = 'message'

    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
