""" Configuration for Flask components """

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """ Provide configuration values from environment or by default """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'guess-you-never-will'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
