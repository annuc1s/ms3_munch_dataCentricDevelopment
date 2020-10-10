# LUNCH at MUNCH...
was inspired by the current Covid-19 situation. When I am not coding I am working in hospitality and we have
a lot of guidelines to follow. A very important guideline is that of contact tracing. My aim with this app 
was to create system where the customer could make a reservation and the business owner would have a list of these 
customers saved to their database, that can then be easily accessed if requested by the HSE. 
I have also noticed a lot of businesses updating and changing their menus as the situation unfolds. For this the 
menu has also been built up out of database so the items and price lists can convenietly be updated.

## UX

This website is for both the customer and the business owner. 

### Customer 

On the landing page the customer can access information about the business, view what they offer on their menu,
engage with the business via contact form and find other contact information. 
They can also make a reservation to visit the restaurant, as well as, remove their reservation.

### Business owner

The business owner chooses what information they wish to display to the customer. They can easily make changes 
to the menu. The business owner also has access to the reservation data which can be used for contact tracing 
if necessary, as well as, allow for judgement on how busy any given day will be at the restaurant. They can 
also engage with customers who contact them with any queries.

### User stories
As a first time visitor to Munch this website is a great source of information. 
I can view their menu and decide if this place offers what I am looking for. If so I can make reservation 
through the landing page or the navigation bar. When I select this option, I am redirected to a sign in page.
Since, I am a new customer and do not yet have an account I have the option to create one, by providing a 
unique username and password. If the username has already been taken by someone else it will no allow me to 
proceed. However, if the username is unique I get access to the reservation form. After enetering my name,
number, date, time, party size and any additional info(optional), I can review the submission that I had just made.
If i am unhappy with any of the information provided, I have the option to delete the reservation and be redirected 
back to the reservation page. If I have any questions an easy to submit application form is accessible from the
nav-bar or the landing page. Other contact details such as google maps and phone number is also easily accessible.
As a returning customer I can go straight to the book table page and just sign in as an account has already been 
created for me. All I have to do then is fill out the reservation form and have some GREAT FOOD.


### Wireframes

My design ideas for this project where ever changing.
I initially imagined the design to be across multiple pages, but then decided against that as it would have had 
too many navigation features. 
    * see initial design wireframes/initial-wireframes.jpg
I then merged the information onto a single landing page, with the exception of the reservation. However, there 
are plenty of prompts for the user to proceed and explore this area.
    * see final design wireframes/final-wireframes.jpg

## Features

### Existing Features

* Navigation-Bar: Allows the user to easily and intuitively navigate the website. It is fixed so as 
    they move down the page it follows and they can at any point change their location on the site.

    * Hero-image & slogan: Create a strong first impression and prompt the user to interact with the button 
    which redirects them to the sign-in page. 

    * About: Gives a short statement about the business further enticing the user.

    * Menu: Menu provides the customer with information on what the restaurant is selling. It can also be 
    quickly updated by the business owner with the database. 

    * Contact Form: Allows the customer to interact with the business by sending an email. An automated response 
    is sent back straight away to let them know that the business has received the email and will answer 
    the query promptly. 

    * Google API: Provides the exact location of the business via google maps. 

    * External Social-Media Links: Invites the customer to follow the businesses social media to keep up to date.

    * Sign-Up: Allows the user to create an account in order to make a reservation.

    * Sign-In: Allows the user to access their existing account in order to make a reservation.

    * Reservation-Form: Allows the user to make a reservation for the restaurant for their prefered time and date.
    It also allows the business owner to view future reservations and retrieve data from the database if necessary.

    * Review-Reservation: Allows the customer to review the reservation they had just made.

    * Delete-Reservation: Will remove the reservation if the user chooses to and will redirect them to 
    reservation-form.


### Features Left to Implement

This website is just a snippet of what I imagine it to be. In the future I hope to expand it:

* I would reuse the menu database collection and build an online ordering system where 
    the user can pre-order their meals.

    * Provide an option to edit customers created reservation not just delete it.

    * If a customer with an account has already made a reservation display it once they log in.

    * Create a live customer review platform. 

    * Flashed messages to give the user some guide if they have done something incorrect eg. if 
    a wrong password/username is provided.

## Technologies Used

In order to create this project I used sever technologies:

* CSS3: Used to add and change default HTLM styling.
    I decided not to use any templates for this project as I wanted to further develop my raw css skills.

    * HTLM5: Was used to create the structure for the app.

    * Javascript: Was used to create functions to make the app more interactive. To create a responsive nav-bar
    introduce EmailJS and GoogleAPI, etc.

    * Python: Used to create the back-end functionality such as the log in and reservations.

    * MongoDB: Was used to create database collections for storing and retrieving information.

    * PyMongo: Allowed for the database from the back-end to be brought to fron-end and styled.

    * Flask: Assisted in writing the Python code.

    * Github: Was used as a remote repository where the changes were commited and pushed to.

    * Gitpod: Was used as an environment for where the code was developed.

    * Heroku: Used to deploy the app.


I used https://fonts.google.com/ to source the fonts for this project. 
fontswesome.com/ was used for icons.

If I came accross an issue I used stackoverflow.com and w3schools.com to see example solutions.
These online resources are reliable and accessible to everyone.

## Testing

The website functions and responds as intended in the UX design. It is responsive to different screen sizes. 
It is simple to navigate due to the consistancy in design. It is interactive and engaging.

    * CSS was put through a code validator and came back without any errors.

    * HTML was put through a code validator and produced couple errors, relating to the database calls 
    (eg.{{snack.item_heading}}). The error is irrelevent and left unchanged. Also, due to the fact that 
    a base.html is used in the production of this app the validator was looking for a DOCTYPE and a head element
    for other html files.
    Any other html errors were addressed.

    * JavaScript files were enteres in JSHint.com and came back without any errors.

    * Python was testes with http://pep8online.com/ no major issues were detected other then syntax spacing
    and commenting. I made recommended adjusments.


The app has been tested in multiple browser such as Chrome, Mozilla and Mi browser(phone browser), OnePlus, Iphone8 
and Amazon Kindle. The deployment has been consistent with minor diffrences in the reservation form with the default
time and date icons not displaying. 
The app has also been tested on multiple screen sizes and is responsive.

In order to keep on top of any issues I constanly was checking the functioning of the app with the preview and 
making commits accordingly to save my progress and changes.


### Features Tested

* The navigation bar is responsive, it brings the user to the correct section of the page;
* All anchor tags open a new page/tab;
* Social media links have a _blank application 
* Contact form cannot be submitted unless all fields are filled out, automated "Please fill in this field" pops up;
* Where applied, hovers are responsive;
* Images display as intended;
* SignUp/SignIn cannot be completed without filling in all fields;
* Reservation form cannot be submitted without filling in all required fields;
* GoogleAPI pins the correct location;
* All templates render as intended;
* If the menu databse is edited it will update the deployed app;
* A document from reservations collection is removed after delete button is activated;
* EmailJS will send an automated response after completing the contact form;
* Content of rows and columns adjust with resizing of screen



To test if JavaScript files are linked correctly I used the dev tools. Dev tools also came in handy when the code
did not run as intended.

To detect any python issues the Git terminal was helpful.

### Bugs addressed

* I was having difficulty with retrieving the reservation data from the collection in order to
loop through it for the review of reservation. I went through many failed versions of this code
before getting it work.

### Bugs not yet addressed

* I was able to create an environment variable for "MongoURI", however, it did not allow me to deploy 
to Heroku if the variable was not visable. I then revealed the variable, I understand that this is 
terrible practice to display sensitive data such as that. However, at this point I was not sure what 
needed to be done and what I was doing incorrectly. I am determined to find what caused the issue and 
not make the same mistake in my future projects.

* I was also having an issue with displaying a backround-image for reviewing the reservation. The code was
the exact copy of book-tbl.html but the image did not show. I have removed the image from review-reservation.html, 
however, it remains in book-tbl.html in order to show what it was supposed to look like. 

## Deployment

The app was deployed on Heroku, in order to do this:
* I needed to create a Heroku app in heroku.com
    * create a requirements.txt file by writing (pip3 freeze --local>requirements.txt) in the terminal
    * create a Procfile by writing (echo web: python app.py>Profile) in the terminal
    * log in to heroku from terminal (heroku login -i)
    * I was then able to deploy the app through heroku.com by opening the app I had created
    * selecting the settings and adding IP and PORT variables
    * then selecting the deploy option option from nav-bar
    * selecting the deployment method to be Github
    * selecting the correct repo from github to connect
    * enable automatic deploys 
    * and deploy the branch 
    * open the app

    * push any future commits through the terminal (git push heroku master) to create up to date app.

In order for others to view my source code, the repository is made public and can be cloned or downloaded 
as necessary. In order to clone they need to use git in a repository terminal (git clone //repositoryURL). 
They can access the cloneable URL link from my github repository.

A specific commit can also be selected in order to track the project progress.

## Credits

### Content
The content and the UX design  was inspired by the current regulations regarding Covid-19 in hospitality setting.

### Media
Images used in this project were obtained from  https://www.pexels.com/

### Acknowledgements

I would like to thank everyone working together to tackle Covid-19 and supporting local businesses.

I would also like to say thanks to my mentor and the amazing Slack community for helping me
 complete this project.