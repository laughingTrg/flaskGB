from flask import Flask

from blog.user import views as user_views
from blog.article import views as article_views
from blog.index import views as index_views

#@app.route('/')
#def index():
#    return "Hello a new web blog!"

def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprints(app)
    return app
    
def register_blueprints(app: Flask):
    app.register_blueprint(user_views.user)
    app.register_blueprint(article_views.article)
    app.register_blueprint(index_views.index)

