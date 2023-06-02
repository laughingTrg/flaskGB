from flask_combo_jsonapi import ResourceDetail, ResourceList

from blog.schemas.tag import TagSchema
from blog.models import Tag
from blog.extenshion import db

class TagList(ResourceList):
    schema = TagSchema
    data_layer = {
            'session': db.session,
            'model': Tag,
            }

class TagDetail(ResourceDetail):
    schema = TagSchema
    data_layer = {
            'session': db.session,
            'model': Tag,
            }

