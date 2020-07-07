import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

# if os.path.exists("env.py"):
#     import env

app = Flask(__name__)
# Config Settings & Environmental Variables located in env.py
app.config['MONGODB_NAME'] = "cookbook"
app.config['MONGO_URI'] = "mongodb+srv://root:pMh9EHCNVwAtL5Y@cluster1-6gani.mongodb.net/cookbook?retryWrites=true&w=majority"


mongo = PyMongo(app)

# MongoDB database variables
users_db = mongo.db.users
recipes_db = mongo.db.recipes
cuisines_db = mongo.db.cuisines
type_db = mongo.db.type
spice_db = mongo.db.spice
difficulty_db = mongo.db.difficulty
mottos_db = mongo.db.mottos
features_db = mongo.db.features

'''
ROUTES
'''

'''
HOME PAGE
'''


@app.route('/')
@app.route('/home')
def home():
    '''
    Main home page.
    '''

    random_motto = ([motto for motto in mottos_db.aggregate
                     ([{"$sample": {"size": 1}}])])
    return render_template('home.html', featured_recipes=features_db,
                           title='Home', random_motto=random_motto)


@app.route('/recipe')
def recipe():
    random_motto = ([motto for motto in mottos_db.aggregate
                     ([{"$sample": {"size": 1}}])])
    return render_template("recipe.html", title='Recipe', random_motto=mongo.db.mottos)


'''
RECIPE PAGE
'''

'''
ADD/EDIT PAGE
'''

'''
SE PAGE
'''


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')), debug=True)
