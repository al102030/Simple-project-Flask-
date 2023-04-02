from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import token

app = Flask(__name__)
app.config['SECRET_KEY'] = token
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
# Your email address that saved in environement varable (bash_profile)
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USERNAME')
# Your email password that saved in environement varable (bash_profile)
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASSWORD')
mail = Mail(app)

from flaskblog.users.routes import users  # noqa: E402
from flaskblog.posts.routes import posts  # noqa: E402
from flaskblog.main.routes import main   # noqa: E402

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)
