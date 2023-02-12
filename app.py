from flask import Flask, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension 
from models import db, connect_db, Pet, DEFAULT_IMG
from forms import AddPetForm, EditPetForm

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

if Pet.query.all() == []:
    woofy = Pet(
        name = 'Woofy',
        species = 'Dog',
        age = 2,
        notes = 'very sweet, likes to play'
    )

    bolt = Pet(
        name = 'Apolo',
        species = 'Cat',
        age = 1,
        notes = 'loves chin scratches'
    )
    cesar = Pet(
        name = 'Cesar',
        species = 'Komodo Dragon',
        age = 2,
        notes = 'super chill'
    )
    pets = [woofy, bolt, cesar]
    db.session.add_all(pets)
    db.session.commit()

@app.route('/')
def root():
    pets = Pet.query.order_by(Pet.id).all()
    return render_template('index.html', pets=pets)

@app.route('/add', methods=['GET','POST'])
def add_pet_form():
    form = AddPetForm()
    if form.validate_on_submit():
        if form.photo_url.data == '':
            form.photo_url.data = DEFAULT_IMG
        pet = Pet(
            name = form.name.data,
            species = form.species.data,
            photo_url = form.photo_url.data,
            age = form.age.data,
            notes = form.notes.data
        )
        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('add-pet-form.html', form=form)

@app.route('/<int:pet_id>')
def pet_details(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    return render_template('pet_details.html', pet=pet)

@app.route('/<int:pet_id>/edit', methods=['GET', 'POST'])
def edit_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect('/')
    else:
        return render_template('/edit-pet-form.html', pet=pet, form=form)
