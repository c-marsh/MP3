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

![Imgur]

</details>
<details>
  <summary>Click to view final screenshot (tablet)!</summary>

![Imgur]

</details>
<details>
  <summary>Click to view final screenshot (desktop)!</summary>

![Imgur]

</details>

### Recipe search / collection
A search box was considered to be easier than having a large checkbox system which also took up a lot of the screen space, especially on smaller screens.
<details>
  <summary>Click to view original wireframe!</summary>


![Imgur](https://i.imgur.com/UGtSLXA.png)
</details>

<details>
  <summary>Click to view final screenshot (mobile)!</summary>

![Imgur]

</details>

<details>
  <summary>Click to view final screenshot (tablet)!</summary>

![Imgur]

</details>

<details>
  <summary>Click to view final screenshot (desktop)!</summary>

![Imgur]

</details>

### Add/Edit Page
The layout has changed as it seemed more intuitive to be adding a title and details first, rather than more detailed information using the checkboxes.
<details>
  <summary>Click to view original wireframe!</summary>

![Imgur](https://i.imgur.com/2OCSc3x.png)
</details>

<details>
  <summary>Click to view final screenshot (mobile)!</summary>

![Imgur]

</details>

<details>
  <summary>Click to view final screenshot (tablet)!</summary>

![Imgur]

</details>

<details>
  <summary>Click to view final screenshot (desktop)!</summary>

![Imgur]

</details>

### Recipe Page
This has to have a design which could handle vastly different amounts of data. As a result, the final page opted for scroll windows for the ingredients and method section, allowing for any amount of text overflow without impacting the design. For mobile views, where the whole page is displayed as in sequence, instead of in columns, this feature is deemed redundant and disabled.
<details>
  <summary>Click to view original wireframe!</summary>

![Imgur](https://i.imgur.com/CLsiTzo.png)

</details>

<details>
  <summary>Click to view final screenshot (mobile)!</summary>

![Imgur]

</details>

<details>
  <summary>Click to view final screenshot (tablet)!</summary>

![Imgur]

</details>

<details>
  <summary>Click to view final screenshot (desktop)!</summary>

![Imgur]

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


Resources
Fonts - https://fonts.google.com/
Allergy Icons - https://erudus.com/standardised-food-allergy-icons/
Side Nav bar - https://colorlib.com/wp/bootstrap-sidebar/
Bootstrap Materialize - https://fezvrasta.github.io/bootstrap-material-design/docs/4.0/material-design/
Default Recipes - BBC Food https://www.bbc.co.uk/food