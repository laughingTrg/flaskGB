from flask import Blueprint, render_template, redirect
from flask_login import login_required
from werkzeug.exceptions import NotFound

author = Blueprint('author', __name__, static_folder='../static', url_prefix='/authors')

@author.route('/')
def author_list():
    from ..models import Author
    authors = Author.query.all()
    return render_template(
        "authors/list.html",
        authors=authors
    )


@author.route('/<int:pk>')
@login_required
def author_detail(pk: int):
    from ..models import Author
    _author = Author.query.filter_by(id=pk).one_or_none()
    if _author is None:
        raise NotFound("Author id:{}, not found".format(pk))
    return render_template(
        "authors/detail.html",
        author=_author
    )

def get_user_name(pk: int):
    if pk in USERS:
        user_name = USERS[pk]['name']
    else:
        raise NotFound(f'User id: {pk}, not found!')
    return user_name

