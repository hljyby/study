import os


class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1234@127.0.0.1:3306/myflask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    STATIC_DIR = os.path.join(BASE_DIR, 'static')
    TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
    UPLOAD_DIR = os.path.join(BASE_DIR, 'upload')


class DevelopmentConfig(Config):
    ENV = 'development'


# ENV = 'development'
# DEBUG = True
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1234@127.0.0.1:3306/myflask'
# SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    ENV = 'production'
