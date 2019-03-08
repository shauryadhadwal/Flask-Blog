import os

class Config:
    SECRET_KEY = '45385b37d4fd30237a8f76696fba1bf3'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///D:\\Projects\\FlaskBlog\\temp\\data.db'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('GMAIL_USER')
    MAIL_PASSWORD = os.environ.get('GMAIL_PASS')
    # MAIL_USE_TLS = True
    # MAIL_PORT = 587