# from the app package (i.e. subdir), import the app variable
# which is a Flask(__name__)
from app import app, db
from app.models import User

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}