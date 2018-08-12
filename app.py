from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators, SelectField, TextField, FileField
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField
import sqlite3

from cnn import NNet

path_to_db = 'db/predictions.db'

nnet = NNet()

app = Flask(__name__)

photos = UploadSet('photos', IMAGES)

species_choices = [('Danaus plexippus','Danaus plexippus'),('Heliconius charitonius','Heliconius charitonius'),('Heliconius erato','Heliconius erato'),('Junonia coenia','Junonia coenia'),('Lycaena phlaeas','Lycaena phlaeas'),('Nymphalis antiopa','Nymphalis antiopa'),('Papilio cresphontes','Papilio cresphontes'),('Pieris rapae','Pieris rapae'),('Vanessa atalanta','Vanessa atalanta'),('Vanessa cardui','Vanessa cardui')]

app.config['UPLOADED_PHOTOS_DEST'] = 'static/img'
configure_uploads(app, photos)


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contribute')
def contribute():
    return render_template('contribute.html')

@app.route('/results')
def results():
    Results = db.get_all_entries()
    return render_template('results.html', Results=Results)

class PredictionDetails(Form):
    photo = FileField('Photo', validators=[FileAllowed(photos, u'Image only!'), FileRequired(u'File was empty!')])
    name = TextField('Name:', validators=[validators.required()])
    email = TextField('Email:', validators=[validators.required()])
    actualTag = SelectField("Tag", choices=species_choices)
    
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    form = PredictionDetails(request.form)

    if request.method == 'POST' and 'photo' in request.files:
        name = request.form['name']
        email = request.form['email']
        filename = photos.save(request.files['photo'])
        print(name, email, filename)
        db.add_prediction_to_db(name,email,filename)
        
        #nnet.run_train()
        # return filename
    return render_template('predict.html', form=form)


class database_object():

    def create_connection(self):
        self.conn = sqlite3.connect(path_to_db)

    def create_table(self):
        self.create_connection()
        c = self.conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS predictions(
            time TEXT,
            name TEXT,
            email TEXT,
            fileLocation TEXT
        );""")
        self.conn.commit()
        self.conn.close()

    def add_prediction_to_db(self, name, email,filename):
        self.create_connection()
        c = self.conn.cursor()
        c.execute("INSERT INTO predictions(time,name, email,fileLocation) VALUES(CURRENT_TIMESTAMP, '" + name + "','" + email + "','" + filename + "');")
        self.conn.commit()
        self.conn.close()

    def get_all_entries(self):
        self.create_connection()
        c = self.conn.cursor()
        cur = c.execute("SELECT * FROM predictions")
        Results = [dict(Time=row[0],
                    Name=row[1],
                    Email=row[2],
                    FileName=row[3]) for row in cur.fetchall()]
        self.conn.close()
        return Results


if __name__ == '__main__':
    db = database_object()
    db.create_table()
    app.run(debug=True)
    