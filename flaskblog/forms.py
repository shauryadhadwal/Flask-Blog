from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flaskblog.models import User
from flask_login import current_user

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        #TODO: Username should be case insensitive
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("Username already taken! Please choose a different one!")

    def validate_email(self, email):
        #TODO: Username should not be checked for lower and upper cases
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("Email already exists! Please choose a different one!")

class LoginForm(FlaskForm):
    email = StringField('Email',validators = [DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
          
class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Upload Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update Account')

    def validate_username(self, username):
        if current_user.username != username.data:
        #TODO: Username should not be checked for lower and upper cases
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError("Username already taken! Please choose a different one!")

    def validate_email(self, email):
        if current_user.email != email.data:
        #TODO: Username should not be checked for lower and upper cases
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError("Email already exists! Please choose a different one!")


class NewPostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])           
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')

class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Reset Password')

    def validate_email(self, email):
        #TODO: Username should be case insensitive
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError("No account with this email exists! Please choose a different one!")


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset')