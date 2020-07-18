This project uses flask and mongoDB to build a site of finding and sharing recipes. It currently features the ability for anyone to add or edit recipes, but has been built so this could be easily expanded to require account authentication in future releases.

# 1. Design
## User Stories
[Imgur](https://i.imgur.com/o7EbGoX.png)

## Wireframes
Here are the original wire frames designed for the project.

The site looks somewhat different as there were issues arising from the original wireframe designs that lead to their further development during implementation.

### Home Page

<details>
  <summary><h1> Home Page </h1></summary>
  
### Home Page
The cards were too small to show full titles at 4 on a screen, and to keep them in keeping with cards on the rest of the site, were redesigned to be able to work everywhere they were needed while showing the necessary content. 
![Imgur](https://i.imgur.com/HQ5oeCo.png)
</details>

### Recipe search
<details>
  <summary>Click to expand!</summary>

### Recipe search / collection
A search box was considered to be easier than having a large checkbox system which also took up a lot of the screen space, especially on smaller screens.
[Imgur](https://i.imgur.com/UGtSLXA.png)
</details>

### Add/Edit Page
<details>
  <summary>Click to expand!</summary>

### Add/Edit Page
The layout has changed as it seemed more intuitive to be adding a title and details first, rather than more detailed information using the checkboxes.
![Imgur](https://i.imgur.com/2OCSc3x.png)
</details>

### Recipe Page
<details>
  <summary>Click to expand!</summary>

### Recipe Page
This has to have a design which could handle vastly different amounts of data. As a result, the final page opted for scroll windows for the ingredients and method section, allowing for any amount of text overflow without impacting the design. For mobile views, where the whole page is displayed as in sequence, instead of in columns, this feature is deemed redundant and disabled.
</details>


Resources
Fonts - https://fonts.google.com/
Allergy Icons - https://erudus.com/standardised-food-allergy-icons/
Side Nav bar - https://colorlib.com/wp/bootstrap-sidebar/
Bootstrap Materialize - https://fezvrasta.github.io/bootstrap-material-design/docs/4.0/material-design/
Default Recipes - BBC Food https://www.bbc.co.uk/food