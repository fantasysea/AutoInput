from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.jinja_env.variable_start_string = "[["
app.jinja_env.variable_end_string = "]]"
print "run gogoogo"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/test.db'
db = SQLAlchemy(app)

from app import views
__all__=["views"]