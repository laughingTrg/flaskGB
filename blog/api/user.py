from flask_combo_jsonapi import ResourceDetail, ResourceList

from blog.schemas import UserSchema
from blog.models import User
from blog.extenshion import db

class UserList(ResourceList):
    schema = UserSchema
    data_layer = {
            'session': db.session,
            'model': User,
            }

class UserDetail(ResourceDetail):
    schema = UserSchema
    data_layer = {
            'session': db.session,
            'model': User,
            }




