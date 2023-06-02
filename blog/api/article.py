from flask_combo_jsonapi import ResourceDetail, ResourceList
from combojsonapi.event.resource import EventsResource

from blog.schemas import ArticleSchema
from blog.models import Article
from blog.extenshion import db

class ArticleListEvents(EventsResource):
    def event_get_count(self):
        return {'count': Article.query.count()}

class ArticleList(ResourceList):
    events = ArticleListEvents
    schema = ArticleSchema
    data_layer = {
            'session': db.session,
            'model': Article,
            }

class ArticleDetail(ResourceDetail):
    schema = ArticleSchema
    data_layer = {
            'session': db.session,
            'model': Article,
            }


