from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    breed = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    contact = db.Column(db.String(50), nullable=False)
    image = db.Column(db.LargeBinary, nullable=True)

    def __repr__(self):
        return f"Pet('{self.name}', '{self.breed}', '{self.description}', '{self.contact}')"


with app.app_context():
    db.create_all()
    print('Database created successfully!')

    # add some fake pets to the database
    pet1 = Pet(name='Fluffy', breed='Golden Retriever', description='Lost in the park', contact='jane@example.com')
    pet2 = Pet(name='Fido', breed='Labrador Retriever', description='Lost in the neighborhood', contact='john@example.com')
    pet3 = Pet(name='Max', breed='German Shepherd', description='Missing since yesterday', contact='jane@example.com')

    # add pets to session
    db.session.add(pet1)
    db.session.add(pet2)
    db.session.add(pet3)

    # commit changes to the database
    db.session.commit()
    print('Added some pets to the database!')

