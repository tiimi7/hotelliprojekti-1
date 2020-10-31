class Config:
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://jokuvaan:12345@localhost:5432/postgres'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
