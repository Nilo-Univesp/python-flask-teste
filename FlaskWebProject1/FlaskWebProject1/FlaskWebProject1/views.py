"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskWebProject1 import app
from FlaskWebProject1.models import Pet


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

# display pets from the database
@app.route('/pets')
def pets():
    pets = Pet.query.all()
    return render_template(
            'pets.html',
            title='Pets',
            year=datetime.now().year,
            message= pets
    )

if __name__ == '__main__':
    app.run(debug=True)


