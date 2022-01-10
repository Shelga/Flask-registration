from flask import Flask, request
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from hashfunction import get_hash

import os


load_dotenv()

uri = os.getenv("DATABASE_URL")  # or other relevant config var
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

# rest of connection code using the connection string `uri`

app = Flask(__name__)

## take environment variables from .env.
uri = os.getenv('DATABASE_URL')
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


migrate = Migrate(app, db)

class Users(db.Model):
    __tablename__ = 'url_shortner'
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(120), unique=True, nullable=False)
    hash = db.Column(db.String(120), unique=True, nullable=False)
 
    def __init__(self, login, hash):
        self.login = login
        self.hash = hash

    def __repr__(self):
        return self.login

db.create_all()


@app.route('/registration', methods = ["POST"])
def get_userdata():
    if request.method == "POST":
        # Receive login, password
        login = request.form.get("login")
        password = request.form.get("password")
        passwordRepite = request.form.get("passwordRepite")
        ## Calling the hash function from the module
        hashPassword = get_hash(password)
        print("hashPassword", hashPassword)

        if not login:
            print("You must provide a login")
        elif not password:
            print("You must provide a password")
        elif password != passwordRepite:
            print("Wrong passwordRepite")

    
   

        ## Create taable and save long login and hash
        # new_user = Users(login=login, hash=hashPassword)
        # db.session.add(new_user)
        # db.session.commit()
   


    return (f"Welcome!{login}")