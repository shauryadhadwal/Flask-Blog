import secrets
import os
from flask import url_for
from flask_mail import Message
from PIL import Image
from flask import current_app
from flaskblog import mail
def save_picture(form_picture):
    """ Method to save uploaded pictures by user to disk
    Also perform actions like resizign etc. before saving to disk
    """ 
    random_hex = secrets.token_hex(8)
    _, file_ext = os.path.splitext(form_picture.filename)
    picture_name = random_hex + file_ext
    #TODO: Change according to deployment environment
    picture_path = os.path.join(current_app.root_path, 'static\\profile_pics', picture_name)
    
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_name

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender='yourname@gmail.com', recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
                {url_for('users.reset_password', token=token, _external=True)}
                If you didn't initiate a reset, then kindly ignore this email and no changes will take place.
                '''
    try:
        mail.send(msg)
    except:
        print('Mail Error')