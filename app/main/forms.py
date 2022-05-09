from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import InputRequired


class ReviewForm(FlaskForm):

    title = StringField('Review title',validators=[InputRequired()])
    review = TextAreaField('Movie review')
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about yourself.', validators=[InputRequired()])
    submit = SubmitField('Submit')
