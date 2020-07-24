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

![Imgur](https://i.imgur.com/aCZupTB.png)

</details>
<details>
  <summary>Click to view final screenshot (tablet)!</summary>

![Imgur](https://i.imgur.com/XPOmLZR.png)

</details>
<details>
  <summary>Click to view final screenshot (desktop)!</summary>

![Imgur](https://i.imgur.com/6EubZpH.png)

</details>

### Recipe search / collection
A search box was considered to be easier than having a large checkbox system which also took up a lot of the screen space, especially on smaller screens.
<details>
  <summary>Click to view original wireframe!</summary>

![Imgur](https://i.imgur.com/UGtSLXA.png)
</details>

<details>
  <summary>Click to view final screenshot (mobile)!</summary>

![Imgur](https://i.imgur.com/EHJOuXZ.png)

</details>

<details>
  <summary>Click to view final screenshot (tablet)!</summary>

![Imgur](https://i.imgur.com/HxCd5Hw.png)

</details>

<details>
  <summary>Click to view final screenshot (including flipped back of card) (desktop)!</summary>

![Imgur](https://i.imgur.com/z7bjXbA.png)

</details>
<details>
  <summary>Click to view search in action!</summary>

![Imgur](https://i.imgur.com/0WOc5nH.gif)

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

![Imgur](https://i.imgur.com/Z2GYfDp.png)
![Imgur](https://i.imgur.com/pbeYr0Y.png)

</details>

<details>
  <summary>Click to view final screenshot (tablet)!</summary>

![Imgur](https://i.imgur.com/mqZoXma.png)

</details>

<details>
  <summary>Click to view final screenshot (desktop)!</summary>

![Imgur](https://i.imgur.com/9CXlEot.png)
![Imgur](https://i.imgur.com/9GgOyk3.png)

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

![Imgur](https://i.imgur.com/L4AF3U4.png)
![Imgur](https://i.imgur.com/DFIWSAs.png)
![Imgur](https://i.imgur.com/nCtCEoB.png)
![Imgur](https://i.imgur.com/9Xc0rvs.png)


</details>

<details>
  <summary>Click to view final screenshot (tablet)!</summary>

![Imgur](https://i.imgur.com/xCYBHQ3.png)
![Imgur](https://i.imgur.com/hwtMY30.png)
</details>

<details>
  <summary>Click to view final screenshot (desktop)!</summary>

![Imgur](https://i.imgur.com/RvStA2w.png)

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

![Imgur](https://i.imgur.com/0XHXH11.png)

</details>
<details>
<summary>Click for example of a recipe card in action</summary>

![Imgur](https://i.imgur.com/hNMh6yH.gif)

</details>

## Other Features
<details>
<summary>Feedback messages are displayed below the Nav bar to confirm user actions such as adding, editing and deleting recipes.</summary>
  
![Imgur](https://i.imgur.com/8b7Eezu.png)

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
The website also uses partial templates for the recipe cards, nav bars and footers to make the website easy to modify as it scales in size. 
The use of templates for recipes means that the number of entries can be unlimited.

#### Further Features to implementation
- User Registration
- User account administration (delete profile/change email/password etc)
- Restrict editing/deleting recipes to the user who added them
- Page to view self submitted recipes
- Ability to bookmark and for a user to review and manage their bookmarked recipes
- Improved search/filtering to filter out allergens

# Testing
## Validation and Compliance
### Front End

https://autoprefixer.github.io/ has been used to ensure CSS is as compatible as possible across a range of devices, but the limitations of using Materialize for Bootstrap are that it only supports IE10+ and iOS 7+ according to it's [documentation](https://fezvrasta.github.io/bootstrap-material-design/docs/4.0/migration/#browser-support). 

The Python code complies with PEP8 standards.

#### Automated Report 
Created by powermapper.com

![Imgur](https://i.imgur.com/lEScNXC.png)

While this looks like a lot of errors, there have been work arounds provided for the ones which actually impact the page which have been described in the sections below.
<details>
  <summary>
Errors</summary>
This section shows no site quality issues, including broken links and server mis-configurations. 

Spell check was not enabled due to to it flagging hundreds of issues with words and names in the recipe content.

</details>

<details>
  <summary>
Accessibility</summary>
This section shows accessibility issues, indicating problems for older users, people with disabilities or accessibility needs. Automated testing cannot detect all accessibility issues, so should be used alongside human testing.

![Imgur](https://i.imgur.com/XxU9aFd.png)

#### Level A
3 issues on 4 pages
<details>
  <summary>Screenreader issues caused by Bootstrap for IE11. Not addressed due to IE11 having such a tiny (1.36%) market share.</summary>

>Content inserted with CSS is not read by some screen readers, and not available to people who turn off style sheets.
>Move the content from CSS to the HTML page so that all users can see it.Impact on users:
> - NVDA 2019.2 IE11 Windows 10 Reading: Text inserted by CSS content property not read.
> - NVDA 2018.4 IE11 Windows 10 Reading: Text inserted by CSS content property not read.
> - NVDA 2017.3 IE11 Windows 10 Reading: Text inserted by CSS content property not read.
> - NVDA 2016.2 IE11 Windows 10 Reading: Text inserted by CSS content property not read.
> - JAWS 2019.1912.1 IE11 Windows 10 Reading: Text inserted by CSS content property not read.
> - JAWS 2018.1811.2 IE11 Windows 10 Reading: Text inserted by CSS content property not read.
> - JAWS 18.0.5038 IE11 Windows 10 Reading: Text inserted by CSS content property not read.
> - JAWS 17.0.2619 IE11 Windows 10 Reading: Text inserted by CSS content property not read.
> 
> http://cmh-cookbook.herokuapp.com/static/css/bootstrap-material-design.css line 3287 3318 
> 
> https://cmh-cookbook.herokuapp.com/static/css/bootstrap-material-design.css line 3287 3318  

Guideline: WCAG 2.1 A F87 Section 508 (2017) A F87  
</details>
<details>
  <summary>The pages with the same title are the route, and home which are both the same page</summary>

> Some pages have the same title, so the title cannot be used to distinguish pages.
> Change the title elements so they are unique for each page.
>' Welcome Page' is also used on https://cmh-cookbook.herokuapp.com/ 
> 
> http://cmh-cookbook.herokuapp.com/home line 50  

Guideline: WCAG 2.1 A F25 Section 508 (2017) A F25  
</details>
<details>
  <summary>Bootstrap uses CSS to apply Bold Fonts</summary>

> Use semantic markup like strong instead of using the CSS font-weight property.
> Use the strong element instead of the span element for bold text.
>
> https://cmh-cookbook.herokuapp.com/ line 202 321 437 559 679 ... 

Guideline: WCAG 2.1 A F2 Section 508 (2017) A F2  
</details>

#### Level AA
2 issues on 5 pages

<details>
  <summary>Colour contrast issues may apply to the card footer on smaller screens, however this is displaying non-essential information and not far from the required ratio.</summary>
	
>Ensure that text and background colors have enough contrast.
>Some users find it hard to read light gray text on a white background, dark gray text on a black background and white text on a red background.
> - The contrast ratio should be 3.0 or more for 18 point text, or larger
> - The contrast ratio should be 3.0 or more for 14 point bold text, or larger
> - The contrast ratio should be 4.5 or more for all other text
> - The text color to background color contrast ratio is: 4.38 with 
>```
>color: rgb(68,68,68);
>background-color: rgb(126,188,137);
>font-size: 12pt;
>font-weight: 400; 
>4.38 with color: rgb(68,68,68);
>background-color: rgb(126,188,137);
>```
>https://cmh-cookbook.herokuapp.com/ line 211 330 447 569 689 ... 

Guideline: WCAG 2.1 AA 1.4.3 Section 508 (2017) AA 1.4.3 
</details>
<details>
  <summary>The outline behaviour is primarily a result of Materialize, however has also been disabled on the cards intentionally, so that they can flip without showing an outline around their container.</summary>

>The CSS outline or border style on this element makes it difficult or impossible to see the dotted link focus outline.
>Change the style to avoid obscuring the focus outline around focusable elements.Using a border or outline style that obscures the focus ring causes problems for keyboard-only users in:
>- Chrome (obscures the focus indicator on links, buttons, dropdowns and range controls)
>- Firefox (obscures the focus indicator on links)
>- Internet Explorer (obscures the focus indicator on links, buttons and range controls)
>- Internet Explorer does not support the `outline-offset:` property, so using this does not reliably avoid focus outline overlap.
>
>http://cmh-cookbook.herokuapp.com/static/css/bootstrap-material-design.css line 74 162 3332 4228 4239 ...
>
>http://cmh-cookbook.herokuapp.com/static/css/style.css line 396 
>
>https://cmh-cookbook.herokuapp.com/ line 65 863 
>
>https://cmh-cookbook.herokuapp.com/static/css/bootstrap-material-design.css line 74 162 3332 4228 4239 ...
>
>https://cmh-cookbook.herokuapp.com/static/css/style.css line 396  

Guideline: WCAG 2.1 AA F78 Section 508 (2017) AA F78  

</details>
</details>
<details>
  <summary>Compatibility</summary>

This section shows pages that exhibit browser-specific behaviour, or trigger browser bugs.

![Imgur](https://i.imgur.com/S0wgNX1.png)

#### Priority 1
No Bugs

#### Priority 2

4 issues on 5 pages

<details>
  <summary>This is a CSS Pseudo Class included with Bootstrap Materialize, but not referenced in this project </summary>

>The `:read-only` CSS pseudo selector is not supported by some browsers.
>The `:read-only` selector is not supported in Internet Explorer, and only supported in Firefox as `:-moz-read-only` .
>
>http://cmh-cookbook.herokuapp.com/static/css/bootstrap-material-design.css line 11561 11563 
>
>https://cmh-cookbook.herokuapp.com/static/css/bootstrap-material-design.css line 11561 11563  

Guideline: [Firefox](https://developer.mozilla.org/en-US/docs/Web/CSS/:read-only)
</details>
<details>
  <summary>backdrop-filter: is a CSS Property included with Bootstrap Materialize, but not referenced in this project</summary>
	
>The CSS `backdrop-filter:` property is not supported by some browsers.
>
>http://cmh-cookbook.herokuapp.com/static/css/bootstrap-material-design.css line 4770 
>
>https://cmh-cookbook.herokuapp.com/static/css/bootstrap-material-design.css line 4770  

Guideline: [Opera](https://developer.mozilla.org/en-US/docs/Web/CSS/backdrop-filter) [Firefox](https://developer.mozilla.org/en-US/docs/Web/CSS/backdrop-filter) [Safari](https://developer.mozilla.org/en-US/docs/Web/CSS/backdrop-filter) [iPhone/iPad](https://developer.mozilla.org/en-US/docs/Web/CSS/backdrop-filter) [Android](https://developer.mozilla.org/en-US/docs/Web/CSS/backdrop-filter)
</details>
<details>
  <summary>filter: CSS Property included with Bootstrap Materialize, but not referenced in this project</summary>

>The CSS `filter:` property is not supported by some browsers.
>
>https://cmh-cookbook.herokuapp.com/ line 8  

Guideline: [iPhone/iPad 9](https://developer.mozilla.org/en-US/docs/Web/CSS/filter)
</details>
<details>
  <summary>transform: CSS Property is not compatible with some older browsers</summary>

>The CSS `transform:` property is not supported by some older browsers.
>
>http://cmh-cookbook.herokuapp.com/static/css/bootstrap-material-design.css line 3211 4829 5246 5252 8317 ...
>
>http://cmh-cookbook.herokuapp.com/static/css/style.css line 409 453 
>
>https://cmh-cookbook.herokuapp.com/ line 8 
>
>https://cmh-cookbook.herokuapp.com/static/css/bootstrap-material-design.css line 3211 4829 5246 5252 8317 ...
>
>https://cmh-cookbook.herokuapp.com/static/css/style.css line 409 453  

Guideline: [iPhone/iPad 8](https://developer.mozilla.org/en-US/docs/Web/CSS/transform)

</details>

#### Priority 3

4 issues on 4 pages

<details>
  <summary>orphans: CSS Property included with Bootstrap Materialize, and is used in features used in the recipe cards in this project</summary>

>The `orphans:` CSS property is not supported by some browsers.
>
>http://cmh-cookbook.herokuapp.com/static/css/bootstrap-material-design.css line 4058 8228
>
>https://cmh-cookbook.herokuapp.com/static/css/bootstrap-material-design.css line 4058 8228  

Guideline: [Firefox](https://developer.mozilla.org/en-US/docs/Web/CSS/orphans) [Safari](https://developer.mozilla.org/en-US/docs/Web/CSS/orphans)
</details>
<details>
  <summary>page-break-after: CSS property is used in Materialize, but not referenced in the project</summary>

>The `page-break-after:` CSS property values `avoid`, `left` and `right` are not supported by Firefox.
>
>http://cmh-cookbook.herokuapp.com/static/css/bootstrap-material-design.css line 8232
>
>https://cmh-cookbook.herokuapp.com/static/css/bootstrap-material-design.css line 8232  

Guideline: [Firefox](https://bugzilla.mozilla.org/show_bug.cgi?id=132035)
</details>
<details>
  <summary>position:sticky CSS property has limited historical browser support</summary>

>The `position:sticky` CSS property is only supported by Firefox 32 and Safari 6.1.
>
>http://cmh-cookbook.herokuapp.com/static/css/bootstrap-material-design.css line 6557 6576 
>
>http://cmh-cookbook.herokuapp.com/static/css/style.css line 218 
>
>https://cmh-cookbook.herokuapp.com/static/css/bootstrap-material-design.css line 6557 6576 
>
>https://cmh-cookbook.herokuapp.com/static/css/style.css line 218  

Guideline: [Chrome](https://developer.mozilla.org/en-US/docs/Web/CSS/position) [Edge](https://developer.mozilla.org/en-US/docs/Web/CSS/position) [Opera](https://developer.mozilla.org/en-US/docs/Web/CSS/position) [Android](https://developer.mozilla.org/en-US/docs/Web/CSS/position)
</details>
<details>
  <summary>widows: CSS Property included with Bootstrap Materialize, and is used in features used in the recipe cards in this project</summary>

>The `widows:` CSS property is not implemented by some browsers.
>
>http://cmh-cookbook.herokuapp.com/static/css/bootstrap-material-design.css line 4059 8229 
>
>https://cmh-cookbook.herokuapp.com/static/css/bootstrap-material-design.css line 4059 8229  

Guideline: [Firefox](https://developer.mozilla.org/en-US/docs/Web/CSS/widows) [Safari](https://developer.mozilla.org/en-US/docs/Web/CSS/widows)
</details>
</details>
<details>
  <summary>Standards</summary>
This section shows pages that do not comply with W3C standards. 

![Imgur](https://i.imgur.com/FUiV2lF.png)

#### Priority 1

3 issues on 2 pages

<details>
  <summary>CSS Validation Error due to code in Materialize. This code has not been addressed as it has been provided as part of the framework.</summary>

>CSS Validation Error.
>
>http://cmh-cookbook.herokuapp.com/static/css/bootstrap-material-design.css line 11393 11394 11395 11396 11400 ...
>
>https://cmh-cookbook.herokuapp.com/static/css/bootstrap-material-design.css line 11393 11394 11395 11396 11400 ... 

![Imgur](https://i.imgur.com/tP9BrMZ.png)

</details>
<details>
  <summary> Invalid CSS selector due to code in Materialize. This code has not been addressed as it has been provided as part of the framework.</summary>
	
>Invalid CSS selector.
>
>http://cmh-cookbook.herokuapp.com/static/css/bootstrap-material-design.css line 11392 
>
>https://cmh-cookbook.herokuapp.com/static/css/bootstrap-material-design.css line 11392  

![Imgur](https://i.imgur.com/m5YRW7e.png)
</details>
<details>
  <summary> Invalid value for CSS property due to code in Materialize. This code has not been addressed as it has been provided as part of the framework.</summary>

>Invalid value for CSS property.
>
>`background: none` 
>
>http://cmh-cookbook.herokuapp.com/static/css/bootstrap-material-design.css line 11037 11654 11871 12048 12225 ...
>
>https://cmh-cookbook.herokuapp.com/static/css/bootstrap-material-design.css line 11037 11654 11871 12048 12225 ... 

![Imgur](https://i.imgur.com/28QTS5l.png)

</details>

#### Priority 2

1 issues on 2 pages
<details>
  <summary>@include used to set default font sizes, in accordance with Bootstrap documentation</summary>

>Unrecognized at-rule.
>The at-rule name may be misspelled or not yet standardized.
>
>`@include`
>
>http://cmh-cookbook.herokuapp.com/static/css/style.css line 45 54 60 
>
>https://cmh-cookbook.herokuapp.com/static/css/style.css line 45 54 60  

</details>

#### Priority 3

1 issues on 2 pages

<details>
  <summary>New CSS properties used</summary>

>Property doesn't exist in CSS.
>The property name may be misspelled, vendor specific, or a new CSS property from a draft specification.
>`text-decoration-skip-ink` `backdrop-filter` 
>
>http://cmh-cookbook.herokuapp.com/static/css/bootstrap-material-design.css line 98 4770 
>
>https://cmh-cookbook.herokuapp.com/static/css/bootstrap-material-design.css line 98 4770 

</details>

#### Informative

These messages are for information only and do not indicate errors

<details>
  <summary>Vendor Specific Properties</summary>

>Property or at-rule is vendor specific.
>Properties and at-rules prefixed by a dash or underscore, the zoom property and the expression() function are vendor specific and only work on one browser engine.
>```
>-webkit-box-sizing -webkit-text-size-adjust -webkit-tap-highlight-color -webkit-box-sizing -webkit-text-decoration -webkit-transition -o-transition -webkit-transition -o-transition -webkit-perspective
>```
>
> http://cmh-cookbook.herokuapp.com/static/css/bootstrap-material-design.css line 51 57 58 77 93 ...
>
>http://cmh-cookbook.herokuapp.com/static/css/style.css line 97 98 115 116 400 ...
>
>https://cmh-cookbook.herokuapp.com/ line 8     
>
>https://cmh-cookbook.herokuapp.com/static/css/bootstrap-material-design.css line 51 57 58 77 93 ...
>
>https://cmh-cookbook.herokuapp.com/static/css/style.css line 97 98 115 116 400 ...  

</details>
</details>
<details>
<summary>Usability</summary>

This section shows general usability issues, indicating navigation problems for all users. 

#### Priority 1
 No Issues

#### Priority 2
6 issues on 161 pages

<details>
  <summary>Underlined text provided as an unused Materialize class</summary>

>Avoid underlined text - people will click on it and think it's a broken link.
>Use something other than underlining for highlighting text, because it looks like a link, and users become frustrated when the "link" does not work.
>
>http://cmh-cookbook.herokuapp.com/static/css/bootstrap-material-design.css line 90 2510 2513 4101 
>
>https://cmh-cookbook.herokuapp.com/static/css/bootstrap-material-design.css line 90 2510 2513 4101  

Guideline: [Usability.gov 10:4](https://guidelines.usability.gov/guidelines/95)

</details>
<details>
<summary>IMG width or height attributes. However all images which are not given a pre-determined height are hidden behind a container with a determined height, ensuring no jumping on loading. </summary>

>Omitting img width or height attributes makes the page layout jump about as images load.
>This makes the page very hard to read or click while it's loading. Fix by adding width and height attributes to the img tag matching the image dimensions. In responsive layouts, specifying width and height prevents layout jumping because the browser can pre-calculate the final image size when CSS like this is used: 
>```
>img {  
>   max-width: 100%; 
>   height: auto;
>}
>``` 
>https://cmh-cookbook.herokuapp.com/ line 71 74 77 80 83 
>
>https://cmh-cookbook.herokuapp.com/add_recipe line 178 188 198 208 218 ...
>
>https://cmh-cookbook.herokuapp.com/home line 433 445 647 659 854 ...
>
>https://cmh-cookbook.herokuapp.com/recipe/5f175cc247049df9349fe429 line 178 188 198 208  ...
>
>https://cmh-cookbook.herokuapp.com/recipe/5f175e9b47049df9349fe42c line 178 347  581 592 ...
>
>https://cmh-cookbook.herokuapp.com/recipe/5f175fb747049df9349fe42e line 178 188 198 347  ...
>
>https://cmh-cookbook.herokuapp.com/recipe/5f17627947049df9349fe432 line 178 347  606 617 ...
>
>https://cmh-cookbook.herokuapp.com/recipe/5f1760a247049df9349fe42f line 178 188 347  661 ...
>
>https://cmh-cookbook.herokuapp.com/recipe/5f17638547049df9349fe433 line 178 347  604 615 ...
>
>https://cmh-cookbook.herokuapp.com/recipe/5f17668347049df9349fe438 line 178 188 347  637 ...
>
>https://cmh-cookbook.herokuapp.com/recipe/5f1767dd47049df9349fe43a line 178 188 198 347  ...
>
>https://cmh-cookbook.herokuapp.com/recipe/5f176c5d6462b9d738c32cc0 line 178 188 198 347  ...
>
>https://cmh-cookbook.herokuapp.com/recipe/5f176d386462b9d738c32cc1 line 178 188 347  641 ...
>
>https://cmh-cookbook.herokuapp.com/recipe/5f176e8c6462b9d738c32cc3 line 178 188 198 347  ...
>
>https://cmh-cookbook.herokuapp.com/recipe/5f17711f6462b9d738c32cc6 line 178 188 347  619 ...
>
>https://cmh-cookbook.herokuapp.com/recipe/5f17722f6462b9d738c32cc8 line 178 347  653 664 ...
>
>https://cmh-cookbook.herokuapp.com/recipe/5f1777c36462b9d738c32ccf line 178 347  554 565 ...
>
>https://cmh-cookbook.herokuapp.com/recipe/5f1778946462b9d738c32cd1 line 178 188 198 208  ...
>
>https://cmh-cookbook.herokuapp.com/recipe/5f1779c06462b9d738c32cd3 line 178 188 198 347  ...
>
>https://cmh-cookbook.herokuapp.com/search line 466 478 679 691 885 ... 

Guideline: [Usability.gov 14:3](https://guidelines.usability.gov/guidelines/152) [W3C](https://developer.mozilla.org/en-US/docs/Web/Media/images/aspect_ratio_mapping)

</details>
<details>
<summary>A search filter is provided on long pages, however as it's a javascript filter the validator doesn't detect it.</summary>

>On long pages, provide a list of contents with links that take users to the corresponding content farther down the page.
>For long pages with distinct sections, add a short, clickable list of sections at the top of the page. This provides a page outline, and allows users to quickly navigate to specific information.
>
>http://cmh-cookbook.herokuapp.com/search line 1
> 
>https://cmh-cookbook.herokuapp.com/search line 1  

Guideline: [Usability.gov 7:3](https://guidelines.usability.gov/guidelines/69) 

</details>
<details>
<summary>A search bar is provided on the Collections page, longer recipe pages would not benefit from a search</summary>

>Provide a search option on each page of content-rich web sites.
>A search option should be provided on all pages where it may be useful - users should not have to return to the homepage to conduct a search. Search engines can be helpful on content-rich web sites, but do not add value on other types of sites.
>
>https://cmh-cookbook.herokuapp.com/ line 1 
>
>https://cmh-cookbook.herokuapp.com/add_recipe line 1 
>
>https://cmh-cookbook.herokuapp.com/home line 1 
>
>https://cmh-cookbook.herokuapp.com/recipe/5f175cc247049df9349fe429 line 1 
>
>https://cmh-cookbook.herokuapp.com/recipe/5f175e9b47049df9349fe42c line 1 
>
>https://cmh-cookbook.herokuapp.com/recipe/5f175fb747049df9349fe42e line 1 
>
>https://cmh-cookbook.herokuapp.com/recipe/5f1760a247049df9349fe42f line 1 
>
>https://cmh-cookbook.herokuapp.com/recipe/5f17617147049df9349fe430 line 1 
>
>https://cmh-cookbook.herokuapp.com/recipe/5f17627947049df9349fe432 line 1 
>
>https://cmh-cookbook.herokuapp.com/recipe/5f17638547049df9349fe433 line 1 
>
>https://cmh-cookbook.herokuapp.com/recipe/5f17668347049df9349fe438 line 1 
>
>https://cmh-cookbook.herokuapp.com/recipe/5f1767dd47049df9349fe43a line 1 
>
>https://cmh-cookbook.herokuapp.com/recipe/5f176c5d6462b9d738c32cc0 line 1 
>
>https://cmh-cookbook.herokuapp.com/recipe/5f176d386462b9d738c32cc1 line 1 
>
>https://cmh-cookbook.herokuapp.com/recipe/5f176e8c6462b9d738c32cc3 line 1 
>
>https://cmh-cookbook.herokuapp.com/recipe/5f17711f6462b9d738c32cc6 line 1 
>
>https://cmh-cookbook.herokuapp.com/recipe/5f17722f6462b9d738c32cc8 line 1 
>
>https://cmh-cookbook.herokuapp.com/recipe/5f1777c36462b9d738c32ccf line 1 
>
>https://cmh-cookbook.herokuapp.com/recipe/5f1778946462b9d738c32cd1 line 1 
>
>https://cmh-cookbook.herokuapp.com/recipe/5f1779c06462b9d738c32cd3 line 1  

Guideline: [Usability.gov 17:4](https://guidelines.usability.gov/guidelines/189)

</details>
<details>
<summary>The landing page (route '/') and '/home' both have the same title, which shouldn't be a problem as they are the same page</summary> This page title is not unique. Each page should have a descriptive and meaningfully different title.

>Title refers to the text displayed on browser tabs, favorites, and in search engines results pages. If two or more pages have the same title, they cannot be differentiated by users or the Favorites capability of the browser.
>' Welcome Page' is also used on https://cmh-cookbook.herokuapp.com/ 
> http://cmh-cookbook.herokuapp.com/home line 50  

Guideline: [Usability.gov 9:2](https://guidelines.usability.gov/guidelines/85)

</details>
<details> 
<summary>aria-label ="search" used instead of label elements because of Materialize search bar construction</summary>


>Use label elements for each data entry field to show what data is expected.
>Make sure each input field has an associated label describing the field.  http://cmh-cookbook.herokuapp.com/search line 370  https://cmh-cookbook.herokuapp.com/search line 370  
	
Guideline: [Usability.gov 13:5](https://guidelines.usability.gov/guidelines/130)  
</details>

### Priority 3

1 issues on 1 pages

<details> 
<summary>Italics have only been used for the motto, which may exceed 70 characters occasionally, but is designed to behave as a logo, not part of the text body</summary>

>Use italic text sparingly - for one or two words or a short phrase.
>Keep runs of styled text to less than 70 characters. When used well, styled text draws attention to important words, but also decreases reading speed by almost twenty percent.
>
>http://cmh-cookbook.herokuapp.com/edit_recipe/5f1760a247049df9349fe42f line 1638 

Guideline: [Usability.gov 11:10](https://guidelines.usability.gov/guidelines/115)  
</details>

#### Priority 4

1 issues on 2 pages

<details> 
<summary>Radio Buttons don't require use, but a clear isn't provided as we want to encourage incorrect selections to be corrected, not removed.</summary>

>Make sure one radio button in a radio button group is always selected. If users can choose not to activate any of the radio button choices, provide a choice labeled 'None'.
>
>http://cmh-cookbook.herokuapp.com/add_recipe line 523 548 573 598 623 ...
>
>http://cmh-cookbook.herokuapp.com/edit_recipe/5f175fb747049df9349fe42e line 941 958 975 

Guideline: [Usability.gov 13:23](https://guidelines.usability.gov/guidelines/10001) 
</details>
</details>

## Manual Testing
### Browser compatibility
The website was tested on Chrome 84, Firefox 78, iOS Safari 13 and Safari 13 and modified to render correctly on each.
Fixes were implemented for Firefox rendering a 1px line on the rear of the flip cards, and bunching the badges over the prep time on the recipe pages.

There remains a minor bug with the footer occasionally flickering slightly on a fast scroll on Firefox instead of scrolling smoothly. Further investigation is needed, but it is likely to be due to how Firefox renders `position: sticky`.

### Responsiveness
The site appears to function well on mobile devices. The hover cards become cards which flip on being tapped.

### CRUD features
CRUD features are functional on all browsers.

## Data Validation/Defensive Design
<details> 
<summary>Data validation on Chrome in mobile view with video showing the criteria of validation and features at play</summary>

![Imgur](https://i.imgur.com/k0dzv1B.gif) [link in case of not rendering](https://i.imgur.com/k0dzv1B.gif)
</details> 
<details> 
<summary>Data validation on Edge in desktop view with video showing the criteria of validation and features at play</summary>

[Imgur](https://i.imgur.com/9SQ5VOu.mp4) [link in case of not rendering](https://i.imgur.com/9SQ5VOu.mp4)
</details> 

Custom 404/500 pages provide error messages along with (hopefully humorous) kitchen based contexts and a button back to safety.

### User Stories
#### Add a recipe
Somebody wishing to add a recipe could click the add button in the bottom right corner of any page, add the details to the recipe in the corresponding fields and then press submit. This will take them to page of the added recipe and provide an alert that the recipe has been added.

#### Search for a recipe
Somebody wishing to search for a recipe could click the "recipes" button in the nav bar on page, search for the recipe they wish using words based around title, cuisine type, words form the description, difficulty, spiciness or dietary details.

#### Edit a recipe
Somebody wishing to edit a recipe could click the "recipes" button in the nav bar on page, search for the recipe they wish to edit, click "more info" on the reverse of the card, which will open the recipe page, and then select edit from drop menu beside the menu title. They can then amend the details to the recipe in the corresponding fields and then press submit. This will take them to page of the added recipe and provide an alert that the recipe has been added.

#### Delete a recipe
Follow the steps of edit a recipe, but select delete from the drop down menu beside the title. If a menu has been provided by the developer, the delete option is greyed out to prevent the database being fully erased. Deletion takes the viewer back to the home page and flashes a confirmation message.

# Deployment
This website was deployed on Heroku and can be found at https://cmh-cookbook.herokuapp.com/

## Heroku Deployment
First login and create your app on the Heroku site, and select a region. Then in the app settings, under ‘Config Vars’ you can set your MONGO_URI as your database, SECRET_KEY as the secret key you use for forms, and IP, and PORT.

You first create a ‘requirements’ file, which lists all the dependencies by typing in the following command in the bash terminal:
```
Pip3 freeze > -v requirements.txt
```

You will then need to create a ‘Procfile’, which lists the process types in an application.:
```
Echo web: python run. py > Procfile
```

This should then be commited to your repository before Pushing to Heroku:
```
Git add . > git commit -m “Setup Heroku” > git push
```

This will update your repository.


Back on the Heroku site, under 'Deploy' , select Select 'Heroku Git'- which allows CLI interaction from the IDE terminal and use the following commands:
```
$ heroku login 
Press any key except q and (key in your credentials in the preview window)
$ git add .
$ git commit -am “initial commit to heroku”
$ git push Heroku master
```


On Heroky, select ‘Open app’ to see your live app.

## Local Deployment
This can be done by clicking ‘clone or download’ on my GitHub Repository.

Then install all the dependencies listed in the requirements.txt file

Create a .gitignore file containing, to prevent sensitive information being revealed in commits.
```
env.py
__pychache__
```
Then create an ‘env.py’ file in the root directory with the following code:
```
import os

os.environ["MONGO_URI"] = "[DB URI HERE]"
os.environ["SECRET_KEY"] = "[A SECRET KEY HERE]"
```

The user should use MongoDB to create a collection ‘cookbook’ with 7 collections as follows:

### Allergens:
The allergens list. Should only be the 14 EU recognised allergens.

 cookbook.allergens:
>  _id: ObjectId(“…”)
>
>  allergen: < string >  

Input into the allergen field must use "_" instead of " ".


### Cuisines:
The cuisine type.

 cookbook.cuisines:
>  _id: ObjectId(“…”)
>
>  cuisine: < string >  

Input into the cuisines field must use "_" instead of " ".

### Dietary Requirements:
Any dietary requirements

 cookbook.diet:
>  _id: ObjectId(“…”)
>
>  diet: < string >  

Input into the diet field must use "_" instead of " ".

### Difficulty:
Difficulty of the recipe

 cookbook.difficulty:
>  _id: ObjectId(“…”)
>
>  difficulty: < string >  


### Mottos:
The catchphrases generated on each page

 cookbook.mottos:
>  _id: ObjectId(“…”)
>
>  motto: < string >  

Input into the motto field must use a space between words.


### Recipes
cookbook.recipes

<details>
<summary>The records are populated by entry through the website, and look like this when they are</summary>

![Imgur](https://i.imgur.com/TOWGaAv.png)
</details>

### Spice:
How Spicy the food is

 cookbook.spice:
>  _id: ObjectId(“…”)
>
>  motto: < string >  

### Type:
Meal type (eg. Breakfast)

 cookbook.type:
>  _id: ObjectId(“…”)
>
>  motto: < string >  




# Credits and Attribution
### Resources
Code snippets been attributed in the code itself.

Fonts - https://fonts.google.com/

Allergy Icons - https://erudus.com/standardised-food-allergy-icons/

Side Nav bar - https://colorlib.com/wp/bootstrap-sidebar/

Bootstrap Materialize - https://fezvrasta.github.io/bootstrap-material-design/docs/4.0/material-design/

Default Recipes - BBC Food https://www.bbc.co.uk/food

Stackoverflow, [the flask mega-tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) and various sites found via Google have been used to clarify questions, as have Akshat Garg my mentor and Cormac Lawlor  as Code Institute Tutor. 
