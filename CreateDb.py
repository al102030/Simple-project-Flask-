#create database
from flaskblog import app, db
app.app_context().push()
db.create_all()