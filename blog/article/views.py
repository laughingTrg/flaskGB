from flask import Blueprint, render_template, redirect

article = Blueprint('article', __name__, static_folder='../static', url_prefix='/articles')

ARTICLES = {
        1: {
            'title': '1st article',
            'text': 'Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...',
            'author':{
                'id': 1,
                'name': 'Mike',
                }
            },
        2: {
            'title': '2nd article',
            'text': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas viverra bibendum metus. Fusce dapibus risus. ',
            'author':{
                'id': 2,
                'name': 'Mary',
                }
            },
        3: {
            'title': '3rd article',
            'text': 'Нет никого, кто любил бы боль саму по себе, кто искал бы её и кто хотел бы иметь её просто потому, что это боль.',
            'author':{
                'id': 3,
                'name': 'Jeremy',
                }
            },
        }

@article.route('/')
def article_list():
    return render_template('articles/list.html',
                           articles=ARTICLES,)

@article.route('/<int:pk>')
def article_detail(pk: int):
    try:
        article = ARTICLES[pk]
    except KeyError:
        return redirect('/articles/')
    return render_template('articles/detail.html',
                           article=article)
