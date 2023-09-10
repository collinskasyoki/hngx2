# Installation

1. Clone the repo
2. Change directory into the person_api directory. For Linux `cd person_api`
3. Install pipenv to your environment
4. Create a virtual env with `pipenv shell`
5. Install requirements `pipenv install`
6. Create database tables `python manage.py migrate`
7. Run the API `python manage.py runserver`

# Read the Documentation

Read the documentation file at:
https://github.com/collinskasyoki/hngx2/blob/main/person_api/DOCUMENTATION.md

# Testing script

- A testing python script is provided for the https://hngx.kasyoki.africa/api/ endpoint and a localhost endpoint. To run it for the public endpoint, use the file test.py [`python test.py`] To run it in a localhost environment, use the test_localhost.py file [`python test_localhost.py`].
- The script uses Python's request library to test all CRUD endpoints and prints the results and their status codes.

# More Information

More details are covered in the DOCUMENTATION.md file linked above.
