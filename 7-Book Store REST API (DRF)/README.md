# Book Store REST API

💡Note: This assignment is part of OSTAD platform's progress evaluation process. This assignment is designed to evaluate your understanding of the following topics covered in
class:

- API & REST API
- GET, POST, PUT, PATCH & DELETE Requests
- ModelViewSet
- Token Authentication
- Filtering
- Searching
- Ordering
- Pagination
- Throttling

# Project Setup Instructions

1. Create a Python virtual environment.

   > python -m venv env

2. Activate the virtual environment.

   > **Bash:** source env/Scripts/activate

3. Install the required packages mentioned in the [<u>requirements.txt</u>](./requirements.txt) file.

   > pip install -r requirements.txt

4. Execute database migration & run the server by executing the `server.sh` shell script file.

   > bash server.sh

💡 **Note:** The server will start at [http://127.0.0.1:8080](http://127.0.0.1:8080). The shell script (_server.sh_) file execute the following commands chronologically.

> python manage.py makemigrations

> python manage.py migrate

> python manage.py runserver 8080

# Required Packages

The following Python packages are required:

- asgiref==3.11.1
- Django==6.0.7
- django-rest-framework==0.1.0
- djangorestframework==3.17.1
- sqlparse==0.5.5
- tzdata==2026.3

This packages are denoted inside the [<u>requirements.txt</u>](./requirements.txt) file inside the project directory.

# How To Run The Project

Execute the following steps to successfully run this project:

1. To implement any changes to database after modifying any Django model class.

   > python manage.py makemigrations

   > python manage.py migrate

2. To run the "**Book Store API**" server.

   > python manage.py runserver 8080

# API Endpoint List

## Book APIs

| Method |    Endpoint     | Description             |
| ------ | :-------------: | ----------------------- |
| GET    |   /api/books/   | Retrieve all books      |
| POST   |   /api/books/   | Create a new book       |
| GET    | /api/books/<id> | Retrieve a single book  |
| PUT    | /api/books/<id> | Update a book           |
| PATCH  | /api/books/<id> | Partially update a book |
| DELETE | /api/books/<id> | Retrieve a single book  |
