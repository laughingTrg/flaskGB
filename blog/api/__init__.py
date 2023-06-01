from flask_combo_jsonapi import Api
from combojsonapi.spec import ApiSpecPlugin

from blog.api.tag import TagList, TagDetail
from blog.api.user import UserList, UserDetail
from blog.api.author import AuthorList, AuthorDetail
from blog.api.article import ArticleList, ArticleDetail

def create_api_spec_plugin(app):
    api_spec_plugin = ApiSpecPlugin(
        app=app,
        tags = {
            'Tag': 'Tag API',
            'User': 'User API',
            'Author': 'Author API',
            'Article': 'Article API',
            }
            )
    return api_spec_plugin


def init_api(app):
    api_spec_plugin = create_api_spec_plugin(app)
    api = Api(app,
              plugins = [
                    api_spec_plugin,
                  ],)

    api.route(TagList, 'tag_list', '/api/tags/')
    api.route(TagDetail, 'tag_detail', '/api/tags/<int:id>/')
    api.route(UserList, 'user_list', '/api/users/')
    api.route(UserDetail, 'user_detail', '/api/users/<int:id>/')
    api.route(AuthorList, 'author_list', '/api/authors/')
    api.route(AuthorDetail, 'author_detail', '/api/authors/<int:id>/')
    api.route(ArticleList, 'article_list', '/api/articles/')
    api.route(ArticleDetail, 'article_detail', '/api/articles/<int:id>/')

    return api
