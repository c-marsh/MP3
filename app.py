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
        "British": request.form.get("BritishCuisine"),
        "Italian": request.form.get("ItalianCuisine"),
        "Mexican": request.form.get("MexicanCuisine"),
        "Spanish": request.form.get("SpanishCuisine"),
        "American": request.form.get("AmericanCuisine"),
        "Latin American": request.form.get("Latin AmericanCuisine"),
        "Caribbean": request.form.get("CaribbeanCuisine"),
        "Japanese": request.form.get("JapaneseCuisine"),
        "South Asian": request.form.get("South AsianCuisine"),
        "Central Asian": request.form.get("Central AsianCuisine"),
        "Chinese": request.form.get("ChineseCuisine"),
        "South-east Asian": request.form.get("South-east AsianCuisine"),
        "Indian": request.form.get("IndianCuisine"),
        "North African": request.form.get("North AfricanCuisine"),
        "African": request.form.get("AfricanCuisine"),
        "Eastern European": request.form.get("Eastern EuropeanCuisine"),
        "Turkish": request.form.get("TurkishCuisine"),
        "Persian": request.form.get("PersianCuisine"),
        "European": request.form.get("EuropeanCuisine"),
        "Middle Eastern": request.form.get("Middle EasternCuisine"),
        "Festive": request.form.get("FestiveCuisine")}
    allergens = {
        "celery": request.form.get("CeleryAllergy"),
        "crustaceans": request.form.get("CrustaceansAllergy"),
        "eggs": request.form.get("EggsAllergy"),
        "fish": request.form.get("FishAllergy"),
        "lupin": request.form.get("LupinAllergy"),
        "milk": request.form.get("MilkAllergy"),
        "molluscs": request.form.get("MolluscsAllergy"),
        "mustard": request.form.get("MustardAllergy"),
        "peanut": request.form.get("PeanutAllergy"),
        "sesame": request.form.get("SesameAllergy"),
        "soya": request.form.get("SoyaAllergy"),
        "sulphur dioxide": request.form.get("Sulphur DioxideAllergy"),
        "treenut": request.form.get("TreenutAllergy"),
        "wheat": request.form.get("WheatAllergy")}

    if request.method == 'POST':
        # after submitting form, insert new recipe
        new_recipe = {
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
        "British": request.form.get("BritishCuisine"),
        "Italian": request.form.get("ItalianCuisine"),
        "Mexican": request.form.get("MexicanCuisine"),
        "Spanish": request.form.get("SpanishCuisine"),
        "American": request.form.get("AmericanCuisine"),
        "Latin American": request.form.get("Latin AmericanCuisine"),
        "Caribbean": request.form.get("CaribbeanCuisine"),
        "Japanese": request.form.get("JapaneseCuisine"),
        "South Asian": request.form.get("South AsianCuisine"),
        "Central Asian": request.form.get("Central AsianCuisine"),
        "Chinese": request.form.get("ChineseCuisine"),
        "South-east Asian": request.form.get("South-east AsianCuisine"),
        "Indian": request.form.get("IndianCuisine"),
        "North African": request.form.get("North AfricanCuisine"),
        "African": request.form.get("AfricanCuisine"),
        "Eastern European": request.form.get("Eastern EuropeanCuisine"),
        "Turkish": request.form.get("TurkishCuisine"),
        "Persian": request.form.get("PersianCuisine"),
        "European": request.form.get("EuropeanCuisine"),
        "Middle Eastern": request.form.get("Middle EasternCuisine"),
        "Festive": request.form.get("FestiveCuisine")}
    allergens = {
        "celery": request.form.get("CeleryAllergy"),
        "crustaceans": request.form.get("CrustaceansAllergy"),
        "eggs": request.form.get("EggsAllergy"),
        "fish": request.form.get("FishAllergy"),
        "lupin": request.form.get("LupinAllergy"),
        "milk": request.form.get("MilkAllergy"),
        "molluscs": request.form.get("MolluscsAllergy"),
        "mustard": request.form.get("MustardAllergy"),
        "peanut": request.form.get("PeanutAllergy"),
        "sesame": request.form.get("SesameAllergy"),
        "soya": request.form.get("SoyaAllergy"),
        "sulphur dioxide": request.form.get("Sulphur DioxideAllergy"),
        "treenut": request.form.get("TreenutAllergy"),
        "wheat": request.form.get("WheatAllergy")}

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
