from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
app.config["SQLALHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

import route

with app.app_context():
      db.create_all()

if __name__ == '__main__':
      app.run(debug=True)