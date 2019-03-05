""" models.py defines ORM model for database interaction """

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db
from app import login

@login.user_loader
def load_user(id):
    """ Look for user in the database """
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    """ User for site authentication """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        """ show the user of the given object """
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        """ store password in hashed form """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """ validate password against hashed form """
        return check_password_hash(self.password_hash, password)
