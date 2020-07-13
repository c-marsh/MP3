import os
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

# if os.path.exists("env.py"):
#     import env

app = Flask(__name__)
# Config Settings & Environmental Variables located in env.py
app.config['MONGODB_NAME'] = "cookbook"
app.config['MONGO_URI'] = "mongodb+srv://root:pMh9EHCNVwAtL5Y@cluster1-6gani.mongodb.net/cookbook?retryWrites=true&w=majority"
app.secret_key = "secret"

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
diet_db = mongo.db.diet
allergens_db = mongo.db.allergens

'''
Function returns a random sample of 1 record from the motto database
'''


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
    recipe = (
        [recipe for recipe in recipes_db.aggregate
         ([{"$sample": {"size": 4}}])])
    random_motto = (
        [motto for motto in mottos_db.aggregate
         ([{"$sample": {"size": 1}}])])
    return render_template(
        'home.html',
        recipe=recipe,
        title='Home',
        random_motto=random_motto)


'''
RECIPE FILTER
'''


@app.route('/search')
def search():
    random_motto = (
        [motto for motto in mottos_db.aggregate
         ([{"$sample": {"size": 1}}])])
    recipe = recipes_db.find()
    return render_template(
        "search.html",
        title='Search',
        recipe=recipe, random_motto=random_motto)


'''
RECIPE PAGE
'''


@app.route('/recipe/<recipe_id>')
def recipe(recipe_id):
    random_motto = (
        [motto for motto in mottos_db.aggregate
         ([{"$sample": {"size": 1}}])])
    recipe = recipes_db.find_one({"_id": ObjectId(recipe_id)})
    return render_template(
        "recipe.html",
        title='Recipe',
        recipe=recipe, random_motto=random_motto)


'''
ADD RECIPE
'''


@app.route('/add_recipe')
def add_recipe():
    """
    Function routes databases to add recipe page
    """
    random_motto = (
        [motto for motto in mottos_db.aggregate
         ([{"$sample": {"size": 1}}])])
    return render_template(
        "add_recipe.html",
        title='Add Recipe',
        cuisines=cuisines_db.find(),
        spice=spice_db.find(),
        diet=diet_db.find(),
        type=type_db.find(),
        difficulty=difficulty_db.find(),
        allergens=allergens_db.find(),
        random_motto=random_motto)


@app.route('/insert_recipe', methods=['GET', 'POST'])
def insert_recipe():
    """
    Function inserts recalls input from form and inserts a new
    record into database.
    """
    # split ingredients and method outputs into lists, convert
    # checkbox outputs to objects
    ingredients = request.form.get("recipe_ingredients").splitlines()
    method = request.form.get("recipe_method").splitlines()

    # Convertcheckbox outputs to objects
    diet = {
        "pescatarian": request.form.get("pescatarianDiet"),
        "vegan": request.form.get("veganDiet"),
        "none": request.form.get("noneDiet"),
        "vegatarian": request.form.get("vegetarianDiet"),
        "kosher": request.form.get("kosherDiet"),
        "gluten": request.form.get("gluten freeDiet"),
        "lacto": request.form.get("lacto freeDiet")}
    allergens = {
        "celery": request.form.get("celeryAllergy"),
        "crustaceans": request.form.get("crustaceansAllergy"),
        "eggs": request.form.get("eggsAllergy"),
        "fish": request.form.get("fishAllergy"),
        "lupin": request.form.get("lupinAllergy"),
        "milk": request.form.get("milkAllergy"),
        "molluscs": request.form.get("molluscsAllergy"),
        "mustard": request.form.get("mustardAllergy"),
        "peanut": request.form.get("peanutAllergy"),
        "sesame": request.form.get("sesameAllergy"),
        "soya": request.form.get("soyaAllergy"),
        "sulphur_dioxide": request.form.get("sulphur_dioxideAllergy"),
        "treenut": request.form.get("treenutAllergy"),
        "wheat": request.form.get("wheatAllergy")}

    if request.method == 'POST':
        # after submitting form, insert new recipe
        new_recipe = {
            "recipe_title": request.form.get("recipe_title").strip(),
            "recipe_description": request.form.get("recipe_description"),
            "recipe_ingredients": ingredients,
            "recipe_method": method,
            "recipe_prep": request.form.get("recipe_prep"),
            "recipe_servings": request.form.get("recipe_servings"),
            "recipe_cuisine": request.form.get("cuisine"),
            "recipe_type": request.form.get("meal"),
            "recipe_diet": diet,
            "recipe_spice": request.form.get("spice"),
            "recipe_difficulty": request.form.get("difficulty"),
            "recipe_allergens": allergens,
            "image": request.form.get("image"),
            "default": "yes"
        }
        insert_recipe_intoDB = recipes_db.insert_one(new_recipe)

        return redirect(url_for(
            "recipe",
            recipe_id=insert_recipe_intoDB.inserted_id))


'''
EDIT RECIPE
'''


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    random_motto = (
        [motto for motto in mottos_db.aggregate
         ([{"$sample": {"size": 1}}])])
    recipe = recipes_db.find_one({"_id": ObjectId(recipe_id)})
    return render_template(
        "edit_recipe.html",
        title='Edit Recipe',
        cuisines=cuisines_db.find(),
        spice=spice_db.find(),
        diet=diet_db.find(),
        type=type_db.find(),
        difficulty=difficulty_db.find(),
        allergens=allergens_db.find(),
        recipe=recipe,
        random_motto=random_motto)


@app.route('/update_recipe/<recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    """
    Function inserts recalls input from form and inserts a new
    record into database.
    """

    # split ingredients and method outputs into lists, convert
    # checkbox outputs to objects
    ingredients = request.form.get("recipe_ingredients").splitlines()
    method = request.form.get("recipe_method").splitlines()

    # Convertcheckbox outputs to objects
    diet = {
        "pescatarian": request.form.get("pescatarianDiet"),
        "vegan": request.form.get("veganDiet"),
        "none": request.form.get("noneDiet"),
        "vegatarian": request.form.get("vegetarianDiet"),
        "kosher": request.form.get("kosherDiet"),
        "gluten": request.form.get("gluten freeDiet"),
        "lacto": request.form.get("lacto freeDiet")}
    allergens = {
        "celery": request.form.get("celeryAllergy"),
        "crustaceans": request.form.get("crustaceansAllergy"),
        "eggs": request.form.get("eggsAllergy"),
        "fish": request.form.get("fishAllergy"),
        "lupin": request.form.get("lupinAllergy"),
        "milk": request.form.get("milkAllergy"),
        "molluscs": request.form.get("molluscsAllergy"),
        "mustard": request.form.get("mustardAllergy"),
        "peanut": request.form.get("peanutAllergy"),
        "sesame": request.form.get("sesameAllergy"),
        "soya": request.form.get("soyaAllergy"),
        "sulphur_dioxide": request.form.get("sulphur_dioxideAllergy"),
        "treenut": request.form.get("treenutAllergy"),
        "wheat": request.form.get("wheatAllergy")}

    if request.method == 'POST':
        # after submitting form, insert new recipe
        recipes_db.update({'_id': ObjectId(recipe_id)}, {
            "recipe_title": request.form.get("recipe_title").strip(),
            "recipe_description": request.form.get("recipe_description"),
            "recipe_ingredients": ingredients,
            "recipe_method": method,
            "recipe_prep": request.form.get("recipe_prep"),
            "recipe_servings": request.form.get("recipe_servings"),
            "recipe_cuisine": request.form.get("cuisine"),
            "recipe_type": request.form.get("meal"),
            "recipe_diet": diet,
            "recipe_spice": request.form.get("spice"),
            "recipe_difficulty": request.form.get("difficulty"),
            "recipe_allergens": allergens,
            "image": request.form.get("image"),
            "default": "yes"
        })
        return redirect(url_for(
            "home"))


'''
DELETE RECIPE
'''


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    if recipes_db.default:
        flash("This recipe is a default recipe and cannot be deleted")
        return redirect(url_for("home"))
    else:
        flash("Recipe deleted")
        recipes_db.delete_one({'_id': ObjectId(recipe_id)})
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')), debug=True)
