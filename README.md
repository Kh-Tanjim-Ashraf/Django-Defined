# <center> Deep Dive into the Django ORM (Object-Relational Mapper) </center>

### Basic Models Structure
> Restaurant, Rating, Sale

### Usage of '<b>RunScript</b>' Command
1. In every battery, create a folder called '__scripts__'.
2. Create a file called '__init__.py' file.
3. Create the script file, inside that file, create the logic inside the '__run()__' function.
4. Install an extension called '__django-extensions__' in order to run the python script.
> pip install django-extensions
5. Use the following command to execute the python script.
> python manage.py runscript <script_file_name>

<small>[Docs Link]('https://www.django-extensions.readthedocs.io/en/latest/runscript.html')</small>


## The '{model}.save()' Method
The __{model}.save()__ method is used for both creating and updating record for database.


## The '{model}.objects.all()' method
To query & fetch <u>all the records</u> from the database using this 'objects' manager.


