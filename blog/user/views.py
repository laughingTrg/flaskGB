from flask import Blueprint, render_template, redirect

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
    return render_template('users/list.html',
                           users=USERS,)

@user.route('/<int:pk>')
def user_detail(pk: int):
    try:
        user = USERS[pk]
    except KeyError:
        return redirect('/users/')
    return render_template('users/detail.html',
                           user=user)
