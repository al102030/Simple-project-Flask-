import os


class Config:
    # Your secret key that saved in environement varable (bash_profile)
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # Your BD URI that saved in environement varable (bash_profile)
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    # Your email address that saved in environement varable (bash_profile)
    MAIL_USERNAME = os.environ.get('EMAIL_USERNAME')
    # Your email password that saved in environement varable (bash_profile)
    MAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
