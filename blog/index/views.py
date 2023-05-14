from flask import Blueprint, render_template, redirect

index = Blueprint('index', __name__, static_folder='../static', url_prefix='/')

@index.route('/')
def index_page():
    return render_template('index.html', endpoint='index')

