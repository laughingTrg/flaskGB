from datetime import datetime
from flask_login import UserMixin
from .app import db

article_tag_association_table = db.Table(
    'article_tag_association',
    db.metadata,
    db.Column('article_id', db.Integer, db.ForeignKey('articles.id'), nullable=False),
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'), nullable=False),
        )

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    is_staff = db.Column(db.Boolean, nullable=False, default=False)
    author = db.relationship("Author", back_populates='user', uselist=False)

    def __init__(self, email, password, first_name, last_name):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return '<User %r>' % (self.email)

class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship("User", back_populates='author')
    articles = db.relationship("Article", back_populates='author')

class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)

    author = db.relationship("Author", back_populates='articles')
    tags = db.relationship("Tag", secondary=article_tag_association_table, back_populates='articles')

class Tag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    articles = db.relationship("Article", secondary=article_tag_association_table, back_populates='tags')

    
