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
        User(email="some@email.com", name='some User', password=generate_password_hash("test"))
            )
    admin = User(email="admin@mail.com", name="Adminych", password=generate_password_hash("123"), is_staff=True)
    db.session.add(admin)
    db.session.commit()

@app.cli.command('create-tags', help='create tags for articles')
def create_tags():
    from blog.models import Tag

    for name in ['flask', 'django', 'python', 'database', 'rest']:
        tag = Tag(name=name)
        db.session.add(tag)
    db.session.commit()
    print('tags was created')
