from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = 'd4cea4219d9cd6d62eb68093'

db = SQLAlchemy(app)
app.app_context().push()

from market import routes