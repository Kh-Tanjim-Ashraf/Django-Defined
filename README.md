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

<small>*Required python-django package: <b>django-extension</b></small>

<small>RunScript | [Docs Link](https://www.django-extensions.readthedocs.io/en/latest/runscript.html)</small>


### Usage of 'shell_plus' Command
`django shell_plus` is an enhanced version of the default Django shell provided by the Django Extensions package. Its primary benefit is that it automatically imports all of the models of a project and several commonly used Django utilities, saving time and effort during development and debugging.

<small>*Required python-django package: <b>django-extension</b></small>

> Command: python manage.py shell_plus --print-sql

<small>NB: Used the '<i>--print-sql</i>' flag in order to view the raw sql of every ORM query.</small>


<small><b>NB:</b> View the git commits to view all the different types of runscript functions implemented in the same <b>orm_scripts.py</b> file.</small>

## The '{model}.save()' Method
The __{model}.save()__ method is used for both creating and updating record for database.
<small>[Commit Link]()</small>


## The '{model}.objects.all()' method
To query & fetch <u>all the records</u> from the database using the 'objects' manager.
<small>[Commit Link]()</small>


## The '{model}.objects.all().first()' method
To query & fetch <u>the first record</u> from the database using the 'objects' manager.
<small>[Commit Link]()</small>


## The '{model}.objects.all().last()' method
To query & fetch <u>the last record</u> from the database using the 'objects' manager.
<small>[Commit Link]()</small>


## The '{model}.objects.all().[0:4]' method
To query & fetch <u>the first five records</u> from the database using the indexing into django queryset.
<small>[Commit Link]()</small>


## The '{model}.objects.create()' method
Create <u>a new record</u> using the '<b>.create()</b>' method. The model fields will be passed as kwargs inside this method.
<small>[Commit Link]()</small>


## The '{model}.objects.count()' method
Count <u>the total number of record(s)</u> using the '<b>.count()</b>' method.
<small>[Commit Link]()</small>