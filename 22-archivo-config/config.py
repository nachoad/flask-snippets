import os

class Config(object):
    SECRET_KEY = 'mi_clave_secreta'

class DevelopmentConfig(Config):
    DEBUG = True