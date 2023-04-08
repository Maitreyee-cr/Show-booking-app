import os
from flask import Flask
from application import config
from application.config import LocalDevelopmentConfig
from application.database import db
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_security import Security, SQLAlchemySessionUserDatastore, SQLAlchemyUserDatastore
from application.models import *
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object(LocalDevelopmentConfig)
db.init_app(app)
app.app_context().push()

# Import all the controllers so they are loaded
from application.controllers import *

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


@app.errorhandler(403)
def not_authorized(e):
    # note that we set the 403 status explicitly
    return render_template('403.html'), 403
with app.app_context():
        db.create_all()
if __name__ == '__main__':
  app.run(debug=True)
