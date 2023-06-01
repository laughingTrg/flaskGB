from flask_combo_jsonapi import ResourceDetail, ResourceList

from blog.schemas import AuthorSchema
from blog.models import Author
from blog.extenshion import db

class AuthorList(ResourceList):
    schema = AuthorSchema
    data_layer = {
            'session': db.session,
            'model': Author,
            }

class AuthorDetail(ResourceDetail):
    schema = AuthorSchema
    data_layer = {
            'session': db.session,
            'model': Author,
            }



