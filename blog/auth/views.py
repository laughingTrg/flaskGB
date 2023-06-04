from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from blog.forms.user import UserRegisterForm, UserLoginForm
from blog.extenshion import db

auth = Blueprint('auth', __name__, static_folder='../static', url_prefix='/auth')


@auth.route('/login', methods=['GET', 'POST'], endpoint='login')
def login():
    form = UserLoginForm(request.form)
    if request.method == 'GET':
        if not current_user.is_authenticated:
            return render_template('auth/login.html', form=form)
        else:
            return redirect("index")

    if request.method == "POST" and form.validate_on_submit():
        from ..models import User

        messages = []
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()
    
        if not user or not check_password_hash(user.password, password):
            messages.append('Check your login details')
            return redirect(url_for('.login', form=form, messages=messages))
        login_user(user)
        return redirect(url_for('user.user_detail', pk=user.id))

@auth.route('/logout', endpoint='logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('.login'))

@auth.route('/register', methods=['GET', 'POST'], endpoint='register')
def register():

    from blog.models import User
    if current_user.is_authenticated:
        return redirect("index")
    error = None
    form = UserRegisterForm(request.form)
    if request.method == "POST" and form.validate_on_submit():

        if User.query.filter_by(email=form.email.data).count():
            form.email.errors.append("email already exists!")
            return render_template("auth/register.html", form=form)

        user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            password=generate_password_hash(form.password.data)
        )
        db.session.add(user)
        try:
            db.session.commit()
        except IntegrityError:
            error = "Could not create user!"
        else:
            login_user(user)
            return redirect("index")
    return render_template("auth/register.html", form=form, error=error)
