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
diet_db = mongo.db.diet
allergens_db = mongo.db.allergens
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
    random_motto = (
        [motto for motto in mottos_db.aggregate
         ([{"$sample": {"size": 1}}])])
    return render_template(
        'home.html',
        featured_recipes=features_db,
        title='Home',
        random_motto=random_motto)


@app.route('/recipe')
def recipe():
    random_motto = (
        [motto for motto in mottos_db.aggregate
         ([{"$sample": {"size": 1}}])])
    return render_template(
        "recipe.html",
        title='Recipe',
        random_motto=mongo.db.mottos)


'''
RECIPE PAGE
'''

'''
ADD RECIPE
'''


@app.route('/add_recipe')
def add_recipe():
    """
    Function routes databases to add recipe page
    """
    return render_template(
        "add_recipe.html",
        title='Add Recipe',
        cuisines=cuisines_db.find(),
        spice=spice_db.find(),
        diet=diet_db.find(),
        type=type_db.find(),
        difficulty=difficulty_db.find(),
        allergens=allergens_db.find())


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
            "image": request.form.get("image")
        }
        insert_recipe_intoDB = recipes_db.insert_one(new_recipe)

        return redirect(url_for(
            "home"))


'''
EDIT RECIPE
'''


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
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
        recipe=recipe)


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
    spice = {
        "mild": request.form.get("mildSpice"),
        "medium": request.form.get("mediumSpice"),
        "hot": request.form.get("hotSpice")}
    difficulty = {
        "easy": request.form.get("easyDiff"),
        "intermediate": request.form.get("intermediateDiff"),
        "hard": request.form.get("hardDiff")}
    meal_type = {
        "breakfast": request.form.get("breakfastMeal"),
        "side": request.form.get("sideMeal"),
        "beverage": request.form.get("beverageMeal"),
        "main": request.form.get("mainMeal"),
        "desert": request.form.get("desertMeal"),
        "snack": request.form.get("snackMeal")}
    cuisine = {
        "british": request.form.get("britishCuisine"),
        "italian": request.form.get("italianCuisine"),
        "mexican": request.form.get("mexicanCuisine"),
        "spanish": request.form.get("spanishCuisine"),
        "american": request.form.get("americanCuisine"),
        "latin_american": request.form.get("latin_americanCuisine"),
        "caribbean": request.form.get("caribbeanCuisine"),
        "japanese": request.form.get("japaneseCuisine"),
        "south_asian": request.form.get("south_asianCuisine"),
        "central_asian": request.form.get("central_asianCuisine"),
        "chinese": request.form.get("chineseCuisine"),
        "south-east_asian": request.form.get("south-east_asianCuisine"),
        "indian": request.form.get("indianCuisine"),
        "north_african": request.form.get("north_africanCuisine"),
        "african": request.form.get("africanCuisine"),
        "eastern_european": request.form.get("eastern_europeanCuisine"),
        "turkish": request.form.get("turkishCuisine"),
        "persian": request.form.get("persianCuisine"),
        "european": request.form.get("europeanCuisine"),
        "middle_eastern": request.form.get("middle_easternCuisine"),
        "festive": request.form.get("festiveCuisine")}
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
            "recipe_cuisine": cuisine,
            "recipe_type": meal_type,
            "recipe_diet": diet,
            "recipe_spice": spice,
            "recipe_difficulty": difficulty,
            "recipe_allergens": allergens,
            "image": request.form.get("image")
        })
        return redirect(url_for(
            "home"))


'''
SE PAGE
'''


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')), debug=True)
