# internship
project for internship

This is the first implementation of internship project by EBS Integrator

# Steps:
1. git clone https://github.com/vitossoRo/internship
2. cd src
3. pip install -r requirements.txt
4. python manage.py createsuperuser
5. enjoy!)

# To test API it's recommended to install Postman aplication
# Before you would like to test API, you should register first.
# After that you should log in under admin account on localhost to get your Authentithication Token, which is required to test API

What can do API:
1. http://127.0.0.1:8000/api/account/register                 # Register a new user;
2. http://127.0.0.1:8000/api/account/login                    # Login in an account;
3. http://127.0.0.1:8000/api/account/properties/update        # Update email or username of the account;
4. http://127.0.0.1:8000/api/blog/<slug>/                     # Obtain details of the shop product, including (title, description, image, published date, username, price and SKU);
5. http://127.0.0.1:8000/api/blog/<slug>/update               # Update characteristics of the shop product;
6. http://127.0.0.1:8000/api/blog/<slug>/delete               # Remove shop product;
7. http://127.0.0.1:8000/api/blog/create                      # Create new shop product;
8. http://127.0.0.1:8000/api/blog/list                        # Get the list of shop products;
9. http://127.0.0.1:8000/api/blog/list?page=#                 # Get product detail on the indicated page
  (where # is a number of page)

  
