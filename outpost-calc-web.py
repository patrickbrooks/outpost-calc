""" Initialize 'flask shell' context """
from app import app, db
from app.models import User

@app.shell_context_processor
def make_shell_context():
    """ Automatically imports modules for 'flask shell' """
    return {'db': db, 'User': User}
