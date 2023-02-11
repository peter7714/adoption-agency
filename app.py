from flask import Flask, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension 
from models import db, connect_db, Pet

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_agency'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = 'lol_secret_key'

app.app_context().push()

debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def root():
    pets = Pet.query.order_by(Pet.name).all()
    return render_template('index.html', pets=pets)