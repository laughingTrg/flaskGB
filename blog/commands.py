from ..wsgi import app, db
from app import cli

@app.cli.command('create-tags')
def create_tags():
    from blog.models import Tag

    for name in ['flask', 'django', 'python', 'database', 'rest']:
        tag = Tag(name=name)
        db.session.add(tag)
    db.session.commit()
    print('tags was created')
