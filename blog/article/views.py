from flask import Blueprint, render_template, redirect, request, url_for
from blog.forms.article import ArticleBaseForm
from blog.forms.user import UserLoginForm
from flask_login import current_user, login_required
from blog.extenshion import db

article = Blueprint('article', __name__, static_folder='../static', url_prefix='/articles')


@article.route('/', methods=['GET'])
def article_list():
    from blog.models import Article
    articles = Article.query.all()
    return render_template('articles/list.html',
                           articles=articles)

@article.route('/<int:pk>')
def article_detail(pk: int):
    from blog.models import Article
    try:
        article = Article.query.filter_by(id=pk).options(
                db.joinedload(Article.tags)).one_or_none()
    except KeyError:
        return redirect('/articles/')
    return render_template('articles/detail.html',
                           article=article)


@article.route('/create', methods=['GET', 'POST'])
@login_required
def create_article():
    from blog.models import Tag
    error = None
    form = ArticleBaseForm(request.form)
    form.tags.choices = [(tag.id, tag.name) for tag in Tag.query.order_by('name')]
    if request.method == 'GET':

        if not current_user.is_authenticated:
            form = UserLoginForm(request.form)
            return render_template('auth/login.html', form=form)

        return render_template('articles/create.html', form=form)


    if form.validate_on_submit():
        from blog.models import Article, Author, Tag

        title = form.title.data
        text = form.text.data
        
        #author = Author.query.filter_by(user_id=current_user.id).first_or_none()

        if not current_user.author:
            author = Author(user_id=current_user.id)
            db.session.add(author)
            #db.session.flush()
            db.session.commit()
        author_id = current_user.author.id

        article = Article(title=title, text=text, author_id=author_id)
        if form.tags.data:
            selected_tags = Tag.query.filter(Tag.id.in_(form.tags.data))
            for tag in selected_tags:
                article.tags.append(tag)
        db.session.add(article)

        try:
            db.session.commit()
        except:
            error = "Could not create user!"
            return render_template('articles/create.html', form=form, error=error)
        else:
            return redirect(url_for(".article_list"))
    
@article.route('/<string:tag>', methods=['GET'])
def articles_by_tag(tag):
    from blog.models import Article, Tag
    filter_tag = Tag.query.filter(Tag.name==tag).one_or_none()
    if filter_tag:
        articles = Article.query.filter(Article.tags.contains(filter_tag))
        return render_template('articles/list.html',
                           articles=articles)
    error = f'For this tag "{tag}": articles are absent yet'
    return render_template('articles/list.html',
                           error=error)



