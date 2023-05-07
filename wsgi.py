from werkzeug.security import generate_password_hash
from blog.app import create_app, db

app = create_app()

if __name__ == '__main__':
    app = create_app()
    app.run(
        host='0.0.0.0',
        debug=True,
            )

@app.cli.command('init-db', help='create all db')
def init_db():
    from blog.models import User
    db.create_all()

@app.cli.command('create-users', help='create-users')
def create_users():
    from blog.models import User
    db.session.add(
        User(email="some@email.com", password=generate_password_hash("test"))
            )
    db.session.commit()
