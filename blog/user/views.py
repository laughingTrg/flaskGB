from flask import Blueprint, render_template, redirect
from flask_login import login_required
from werkzeug.exceptions import NotFound

user = Blueprint('user', __name__, static_folder='../static', url_prefix='/users')

USERS = {
        1: {
            'name': 'Mike',
            },
        2: {
            'name': 'Mary',
            },
        3: {
            'name': 'Jeremy',
            },
        }

@user.route('/')
def user_list():
    from ..models import User
    users = User.query.all()
    return render_template(
        "users/list.html",
        users=users
    )


@user.route('/<int:pk>')
@login_required
def user_detail(pk: int):
    from ..models import User
    _user = User.query.filter_by(id=pk).one_or_none()
    if _user is None:
        raise NotFound("User id:{}, not found".format(pk))
    return render_template(
        "users/detail.html",
        user=_user
    )

def get_user_name(pk: int):
    if pk in USERS:
        user_name = USERS[pk]['name']
    else:
        raise NotFound(f'User id: {pk}, not found!')
    return user_name
