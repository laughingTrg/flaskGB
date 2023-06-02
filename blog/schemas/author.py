from combojsonapi.utils import Relationship
from marshmallow_jsonapi import Schema, fields

class AuthorSchema(Schema):
    class Meta:
        type_ = 'author'
        self_view = 'author_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'author_list'

    id = fields.Integer(as_string=True)

    articles = Relationship(
        nested='ArticleSchema',
        atribute='artciles',
        relared_view='artcile_detail',
        related_view_kwargs={'id': '<id>'},
        schema='ArticleSchema',
        type_='article',
        many=True,
        )

    user = Relationship(
        nested='UserSchema',
        atribute='user',
        relared_view='user_detail',
        related_view_kwargs={'id': '<id>'},
        schema='UserSchema',
        type_='user',
        many=False,
        )
