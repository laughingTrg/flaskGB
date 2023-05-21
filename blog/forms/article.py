from flask_wtf import FlaskForm
from wtforms import StringField, validators, TextAreaField, SubmitField, SelectMultipleField 

class ArticleBaseForm(FlaskForm):
    title = StringField('Title', [validators.DataRequired()])
    text = TextAreaField('Article text', [validators.DataRequired()])
    tags = SelectMultipleField('Tags', coerce=int)
    submit = SubmitField('Create')
