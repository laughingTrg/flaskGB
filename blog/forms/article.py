from flask_wtf import FlaskForm
from wtforms import StringField, validators, TextAreaField, SubmitField 

class ArticleBaseForm(FlaskForm):
    title = StringField('Title', [validators.DataRequired()])
    text = TextAreaField('Article text', [validators.DataRequired()])
    submit = SubmitField('Create')
