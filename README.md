# CS50 WEB PROGRAMMING FINAL PROJECT: Hand-Made

## Main idea

I have created a web application that helps people who have a hand-made work to post and sell their creative and professional trade. The main contents are the following Pages:

- Home Page: It simply has ```<!DOCTYPE>``` declaration, links of Css and javaScript, navbar and footer and also other Pages which are displayed according to what users may need.

- Header Page: It represents a navbar that contains all information about the website like LOGO, categories, profile user, login, logout, search bar, favourite and cart icons.

- Footer Page: It has links such as home, services, about, terms, privacy policy and social media icons.

- Login, Logout Page and Register Page

- All Products Page: It contains all hand-made items.

- Category Page: It helps any user to choose a certain product.

- Search Page

- Product details Page

- Favourite Page: It includes the products which are preferred by any customer.

- Cart Page

- Add Product Page: It can be used only by admins in order to add new products.

## Distinctiveness and Complexity

Regarding distinctiveness, this website is Considered to be different from others due to its simplicity and clarity. Furthermore there are many options which enable any user to get access easily to certain pages.

Concerning complexity, there are Several steps have been done after completing all the requirements.     Firstly, a user-flow (algorithm for website) by using BPMN program has been performed to include all the properties in the Project and to make sure that browsing the website is so easy for users.
Secondly, UI and UX (user interface and user expression) have been done by using Figma program to get an initial design for the website through Formatting colours, fonts, and dimensions.
Django framework, which is structured by Python, has been used for the backend to have four models (as will be mentioned later).
Finally, in order to set up a complete website that has a simple and beautiful interface, the frontend has been accomplished by using HTML, CSS, BootStrap and Javascript.

## Files information

- In views.py there is all of the backend code. The main functions are:
  - home with all the dynamic data obtained from the database.
  - add_remove_favorite: for add or remove the product from the customer profile.
  - addProduct: for stabilization the admin to add new hand-made product.
  - cart_for_user: for management cart user page.
  - add_quantity: for add more a quantity when user add the product to cart.
  - sub_quantity: for minmize a quantity when user add the product to cart.
  - user_favorites: for management favorite user page.
  - product_details: to view all details about the product.
  - add_remove_to_cart: for add or remove the product from cart.
  - search: for advanced search.
  - categoreis: To views the hand-made product in groups by categories.
  - chooes_category: To select a category from the list of categoreis.
  - contact for contact page.

 - Models.py. The different models are:
 
   - A Customer model
   - A Categories model
   - A Product model

- Index.js:

  - handle click event when adding to favorites page.
  - handle click event when removing from favorites page.
  - handle click event when adding the product to user cart.
  - handle click event when removing the product from user cart.

- Templates for all of the different html pages.

- Style.css: contain the theme and common clases for each html page.

- Other files like urls, admin, settings…

## How to run the application

 - Install project dependencies by running pip install -r requirements.txt.
- Make and apply migrations by running python manage.py makemigrations and python manage.py migrate.
- Run the server by running python manage.py runserver.
- Make sure to create a new superuser and fill the website content through admin dashboard.

