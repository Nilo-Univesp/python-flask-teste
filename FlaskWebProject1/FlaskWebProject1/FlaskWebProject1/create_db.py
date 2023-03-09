from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from FlaskWebProject1.models import Pet

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pets.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db = SQLAlchemy(app)

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

    return app