from flask_wtf import FlaskForm
from wtforms import TextField,TextAreaField
from wtforms.validators import DataRequired

class Postform(FlaskForm):
    title = TextField(validators=[DataRequired()],render_kw={"placeholder":"title"})
    summary = TextAreaField(validators=[DataRequired()],render_kw={"placeholder":"summary"})
    content = TextAreaField(validators=[DataRequired()],render_kw={"placeholder":"content"})
    slug = TextField(validators=[DataRequired()],render_kw={"placeholder":"slug"})
