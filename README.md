This project uses flask and mongoDB to build a site of finding and sharing recipes. It currently features the ability for anyone to add or edit recipes, but has been built so this could be easily expanded to require account authentication in future releases.

# Design
## User Stories
<details>
  <summary>Click to view user Stories!</summary>

![Imgur](https://i.imgur.com/o7EbGoX.png)
</details>

## Site design
The site structure was designed to include further expansion of a user log in and administration system.
<details>
  <summary>Click to view full overall site map!</summary>

![Imgur](https://i.imgur.com/1zSdFJ2.png)
</details>

## Pages

The site looks somewhat different as there were issues arising from the original wireframe designs that lead to their further development during implementation.

### Home Page
The cards were too small to show full titles at 4 on a screen, and to keep them in keeping with cards on the rest of the site, were redesigned to be able to work everywhere they were needed while showing the necessary content.

<details>
  <summary>Click to view original wireframe!</summary>
  
![Imgur](https://i.imgur.com/HQ5oeCo.png)
</details>

<details>
  <summary>Click to view final screenshot (mobile)!</summary>

![Imgur](https://i.imgur.com/aCZupTBm.png)

</details>
<details>
  <summary>Click to view final screenshot (tablet)!</summary>

![Imgur](https://i.imgur.com/XPOmLZRm.png)

</details>
<details>
  <summary>Click to view final screenshot (desktop)!</summary>

![Imgur](https://i.imgur.com/6EubZpHm.png)

</details>

### Recipe search / collection
A search box was considered to be easier than having a large checkbox system which also took up a lot of the screen space, especially on smaller screens.
<details>
  <summary>Click to view original wireframe!</summary>

![Imgur](https://i.imgur.com/UGtSLXA.png)
</details>

<details>
  <summary>Click to view final screenshot (mobile)!</summary>

![Imgur](https://i.imgur.com/EHJOuXZm.png)

</details>

<details>
  <summary>Click to view final screenshot (tablet)!</summary>

![Imgur](https://i.imgur.com/HxCd5Hwm.png)

</details>

<details>
  <summary>Click to view final screenshot (including flipped back of card) (desktop)!</summary>

![Imgur](https://i.imgur.com/z7bjXbAm.png)

</details>

#### Features
The search box acts as a live filter using JS to search the title, description, cuisine, difficulty or diet. As it's just a keyword search, it isn't useful to filter out allergens, however this could be implemented easily using a checkbox and javascript filter.

<details>
  <summary>See it in action</summary>

[Imgur](https://i.imgur.com/0WOc5nH.gif)

</details>

### Add/Edit Page
The layout has changed as it seemed more intuitive to be adding a title and details first, rather than more detailed information using the checkboxes.
<details>
  <summary>Click to view original wireframe!</summary>

![Imgur](https://i.imgur.com/2OCSc3x.png)
</details>

<details>
  <summary>Click to view final screenshot (mobile)!</summary>

![Imgur](https://i.imgur.com/Z2GYfDpm.png)
![Imgur](https://i.imgur.com/pbeYr0Ym.png)

</details>

<details>
  <summary>Click to view final screenshot (tablet)!</summary>

![Imgur](https://i.imgur.com/mqZoXmam.png)

</details>

<details>
  <summary>Click to view final screenshot (desktop)!</summary>

![Imgur](https://i.imgur.com/9CXlEotm.png)
![Imgur](https://i.imgur.com/9GgOyk3m.png)

</details>

#### Features
The form fields require a minimum level of server side validation, to ensure consistency on what is being entered in to the database. Feedback is provided to the user about this, with the commonly used asterisks marking required fields, instructional information below the fields, and tooltips with guidance on attempted submission of illegal data.

While a cancel button was initially provided on the add page, [arguments](https://www.nngroup.com/articles/reset-and-cancel-buttons/) exist about their redundancy in forms, and that they can cause confusion and do not provide useful user information on what they will actually do. In lieu, the navigation menu is available. The cancel button is still provide for edit page, as users may wish to abandon an edit they're making.

### Recipe Page
This has to have a design which could handle vastly different amounts of data. As a result, the final page opted for scroll windows for the ingredients and method section, allowing for any amount of text overflow without impacting the design. For mobile views, where the whole page is displayed as in sequence, instead of in columns, this feature is deemed redundant and disabled.
<details>
  <summary>Click to view original wireframe!</summary>

![Imgur](https://i.imgur.com/CLsiTzo.png)

</details>

<details>
  <summary>Click to view final screenshot (mobile)!</summary>

![Imgur](https://i.imgur.com/L4AF3U4m.png)
![Imgur](https://i.imgur.com/DFIWSAsm.png)
![Imgur](https://i.imgur.com/nCtCEoBm.png)
![Imgur](https://i.imgur.com/9Xc0rvsm.png)


</details>

<details>
  <summary>Click to view final screenshot (tablet)!</summary>

![Imgur](https://i.imgur.com/xCYBHQ3m.png)
![Imgur](https://i.imgur.com/hwtMY30m.png)
</details>

<details>
  <summary>Click to view final screenshot (desktop)!</summary>

![Imgur](https://i.imgur.com/RvStA2wm.png)

</details>

#### Features

<details>
  <summary>Click for example of method/ingredient scrolls which have been implemented to standardise page looks no matter how much content</summary>

![Imgur](https://i.imgur.com/7JCVJe1m.gif)

</details>

<details>
  <summary>Click for example of allergen index in action. This is to show a key for the allergens.</summary>

![Imgur](https://i.imgur.com/Gz1ZlXTm.gif)

</details>
<details>
  <summary>Click for example of edit/delete menu</summary>

![Imgur](https://i.imgur.com/0XHXH11m.png)

</details>

<summary>Click for example of a recipe card in action</summary>

![Imgur](https://i.imgur.com/hNMh6yH.gifv)

</details>

## Visual Language
The site sticks to a visual design based around a set colour scheme 

<details>
  <summary>Click to see design concepts!</summary>

![Imgur](https://i.imgur.com/AoPG2R5.png)

</details>

## Under the Hood
The technologies used to build this website are:
- Gitpod as an IDE
- Materialize for Bootstrap as a framework 
- Javascript - primarily for the search filter, and visual touches
- Python3 using flask framework which also uses the following extensions: 
  * click==7.1.2
  * dnspython==1.16.0
  * Flask==1.1.2
  * Flask-PyMongo==2.3.0
  * Flask-WTF==0.14.3
  * itsdangerous==1.1.0
  * pymongo==3.10.1
  * Werkzeug==1.0.1
  * WTForms==2.3.1
- Jinja2

### Database design
The site uses a no-SQL database

<details>
  <summary>Click to see database design!</summary>

The coloured databases have been built, but are for future implementation in the website.
![Imgur](https://i.imgur.com/BOLw6MS.png)
</details>

<details>
  <summary>Click to see an actual recipe database document!</summary>

Here it can be seen how the method and ingredients are stored as an array, and how the information about allergens, and diets are saved as a objects.

Because these are built referencing another database of dietary requirements, it would be easy to add new dietary requirements to the data dietary requirement database without impacting how the documents handle it.
![Imgur](https://i.imgur.com/TOWGaAv.png)
</details>

### File Structure/Naming Conventions
Because the Recipes database doesn't save filenames for allergen icons, or card thumbnails, a strict naming convention for images has to be stuck to which corresponds to the field name.
<details>
  <summary>
Here's an example showing how the card thumbnails are created using the document information:</summary>

` <img
          src="{{ url_for('static', filename='images/thumbs/')
        }}{{recipe.recipe_type}}.png"
          alt="{{recipe.recipe_type}}"
        />`
</details>

<details>
  <summary>
A screenshot of filenames for comparison</summary>

![Imgur](https://i.imgur.com/2fLIgT0.png)

</details>

### Future Development
The website also uses partial templates for the recipe cards, nav bars and footers to make the website easy to modify as it scales in size. The use of templates for recipes means that the number of entries can be unlimited, and while currently there is no user registration, this could be implemented in the next sprint.

# Testing
## Validation and Compliance
Validator results

## Data Validation
CRUD features

## Manual Testing
Browser compatibility
Responsiveness
Defensive Design

# Deployment

# Credits and Attribution
Resources
Fonts - https://fonts.google.com/
Allergy Icons - https://erudus.com/standardised-food-allergy-icons/
Side Nav bar - https://colorlib.com/wp/bootstrap-sidebar/
Bootstrap Materialize - https://fezvrasta.github.io/bootstrap-material-design/docs/4.0/material-design/
Default Recipes - BBC Food https://www.bbc.co.uk/food