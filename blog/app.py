from os import getenv, path
from flask import Flask
from json import load
#from .models import User

from blog.user import views as user_views
from blog.article import views as article_views
from blog.index import views as index_views
from blog.auth import views as auth_views
from blog.extenshion import db, login_manager

CONFIG_PATH = getenv("CONFIG_PATH", path.join("../config.json"))

def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_file(CONFIG_PATH, load)
    register_extenshions(app)
    register_blueprints(app)
    return app
    
def register_blueprints(app: Flask):
    app.register_blueprint(user_views.user)
    app.register_blueprint(article_views.article)
    app.register_blueprint(index_views.index)
    app.register_blueprint(auth_views.auth)


def register_extenshions(app: Flask):
    db.init_app(app)

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        from .models import User
        return User.query.get(int(user_id))
