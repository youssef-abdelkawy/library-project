from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired

class BookForm(FlaskForm):
    student_name = StringField("Your Name", validators=[DataRequired()])
    book_name = StringField("Book Name", validators=[DataRequired()])
    category = SelectField("Category", choices=[
        ('Programming', 'Programming'),
        ('Sci-Fi', 'Sci-Fi'),
        ('Romance', 'Romance'),
        ('Mystery', 'Mystery'),
        ('Fantasy', 'Fantasy'),
        ('Non-Fiction', 'Non-Fiction')
    ])
    submit = SubmitField("Submit")
