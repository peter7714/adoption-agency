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

if Pet.query.order_by(Pet.name).all() == []:
    woofy = Pet(
        name = 'Woofy',
        species = 'pomchi',
        age = 2,
        notes = 'very sweet, likes to play'
    )

    bolt = Pet(
        name = 'Bolt',
        species = 'bulldog',
        age = 1,
        notes = 'loves to go on walks'
    )
    cesar = Pet(
        name = 'Cesar',
        species = 'Lomodo Dragon',
        age = 2,
        notes = 'super chill'
    )
    pets = [woofy, bolt, cesar]
    db.session.add(pets)
    db.session.commit()

@app.route('/')
def root():
    pets = Pet.query.order_by(Pet.name).all()
    return render_template('index.html', pets=pets)