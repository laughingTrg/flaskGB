from combojsonapi.utils import Relationship
from marshmallow_jsonapi import Schema, fields

class ArticleSchema(Schema):
    class Meta:
        type_ = 'article'
        self_view = 'article_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'article_list'

    id = fields.Integer(as_string=True)
    title = fields.String(allow_none=False)
    body = fields.String(allow_none=False)
    dt_created = fields.DateTime(allow_none=False)
    dt_updated = fields.DateTime(allow_none=False)

    tags = Relationship(
        nested='TagSchema',
        atribute='tags',
        relared_view='tag_detail',
        related_view_kwargs={'id': '<id>'},
        schema='TagSchema',
        type_='tag',
        many=True,
        )

    author = Relationship(
        nested='AuthorSchema',
        atribute='author',
        relared_view='author_detail',
        related_view_kwargs={'id': '<id>'},
        schema='AuthorSchema',
        type_='author',
        many=False,
        )
