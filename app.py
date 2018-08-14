from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators, SelectField, TextField, FileField, IntegerField
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField
import sqlite3
from threading import Thread 
import os

from cnn import NNet

from databasehelper import database_object
from dbrunner import DB_Runner


#nnet = NNet()

app = Flask(__name__)

photos = UploadSet('photos', IMAGES)

species_choices = [('Danaus plexippus','Danaus plexippus'),('Heliconius charitonius','Heliconius charitonius'),('Heliconius erato','Heliconius erato'),('Junonia coenia','Junonia coenia'),('Lycaena phlaeas','Lycaena phlaeas'),('Nymphalis antiopa','Nymphalis antiopa'),('Papilio cresphontes','Papilio cresphontes'),('Pieris rapae','Pieris rapae'),('Vanessa atalanta','Vanessa atalanta'),('Vanessa cardui','Vanessa cardui')]
img_aug_choices = [('YES','YES'),('NO','NO')]

app.config['UPLOADED_PHOTOS_DEST'] = 'static/img'
configure_uploads(app, photos)

class PredictionDetails(Form):
    photo = FileField('Photo', validators=[FileAllowed(photos, u'Image only!'), FileRequired(u'File was empty!')])
    name = TextField('Name:', validators=[validators.required()])
    email = TextField('Email:', validators=[validators.required()])

class ContributionDetails(Form):
    photo = FileField('Photo', validators=[FileAllowed(photos, u'Image only!'), FileRequired(u'File was empty!')])
    name = TextField('Name:', validators=[validators.required()])
    species = SelectField('Species:', choices=species_choices)

class TrainingField(Form):
    noe = IntegerField('Number Of Epochs', validators=[validators.required(), validators.NumberRange(min=0, max=10)])
    imgaug = SelectField('With Image Augmentation:', choices=img_aug_choices)
    modelname = TextField('Model Name:', validators=[validators.required()])

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/training', methods=['GET', 'POST'])
def training():

    form = TrainingField(request.form)
    if request.method == 'POST':
        noe = int(request.form['noe'])
        imgaug = request.form['imgaug']
        modelname = request.form['modelname']
        print(noe,imgaug,modelname)

        nnet = NNet()
        nnet.run_train(noe,modelname)
        return render_template('thanks.html')

    return render_template('training.html', form=form)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/models')
def models():
    return render_template('models.html')

@app.route('/contribute', methods=['GET', 'POST'])
def contribute():
    form = ContributionDetails(request.form)
    if request.method == 'POST' and 'photo' in request.files:
        name = request.form['name']
        species = request.form['species']
        filename = photos.save(request.files['photo'],species)
        print(name, species)
        return render_template('thanks.html')

    return render_template('contribute.html', form=form)

@app.route('/thanks')
def thanks():
    return render_template('thanks.html')

@app.route('/results')
def results():
    Results = db.get_all_entries()
    return render_template('results.html', Results=Results)


    
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    form = PredictionDetails(request.form)

    if request.method == 'POST' and 'photo' in request.files:
        name = request.form['name']
        email = request.form['email']
        filename = photos.save(request.files['photo'])
        print(name, email, filename)
        db.add_prediction_to_db(name,email,filename)
        dbrunner = DB_Runner()
        return render_template('thanks.html')
    
    return render_template('predict.html', form=form)



if __name__ == '__main__':
    db = database_object()
    db.create_table()
    db.create_model_table()
    app.run(debug=True,host='0.0.0.0',port=25565)
    