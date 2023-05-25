from flask_wtf import FlaskForm
from wtforms.fields import SubmitField
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, Optional, URL


class MessageForm(FlaskForm):
    """Form for adding/editing messages."""

    text = TextAreaField('text', validators=[DataRequired()])


class UserAddForm(FlaskForm):
    """Form for adding users."""

    username = StringField('Username', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[Length(min=6)])
    image_url = StringField('(Optional) Image URL', validators=[Optional(), URL()])
    bio = TextAreaField('Bio', validators=[Optional()])
    location = StringField('Location', validators=[Optional()])
    header_image_url = StringField('Header Image URL', validators=[Optional(), URL()])


class UserEditForm(FlaskForm):
    """Form for adding users."""

    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    image_url = StringField('(Optional) Image URL')
    bio = TextAreaField('Bio')
    location = StringField('Location')
    header_image_url = StringField('Header Image URL')
    password = PasswordField('Password', validators=[Length(min=6)])

class UserUpdateForm(FlaskForm):
    """Form for updating users."""

    username = StringField('Username', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    image_url = StringField('Image URL')
    header_image_url = StringField('Header Image URL')
    bio = TextAreaField('Bio')
    location = StringField('Location')
    password = PasswordField('Password', validators=[Length(min=6)])



class LoginForm(FlaskForm):
    """Login form."""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6)])
