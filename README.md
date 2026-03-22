# <center> Deep Dive into the Django ORM (Object-Relational Mapper) </center>

## 1. Querying, Creating Records & Working with Foreign Keys 

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

<small>RunScript | [Docs Link](https://django-extensions.readthedocs.io/en/latest/runscript.html)</small>


### Usage of '<b>shell_plus</b>' Command
`django shell_plus` is an enhanced version of the default Django shell provided by the Django Extensions package. Its primary benefit is that it automatically imports all of the models of a project and several commonly used Django utilities, saving time and effort during development and debugging.

<small>*Required python-django package: <b>django-extension</b></small>

> Command: python manage.py shell_plus --print-sql

<small>NB: Used the '<i>--print-sql</i>' flag in order to view the raw sql of every ORM query.</small>


<small><b>NB:</b> View the git commits to view all the different types of runscript functions implemented in the same <b>orm_scripts.py</b> file.</small>

### The '{model}.save()' Method
The __{model}.save()__ method is used for both creating and updating record for database.
<small>[Commit Link]()</small>


### The '{model}.objects.all()' method
To query & fetch <u>all the records</u> from the database using the 'objects' manager.
<small>[Commit Link]()</small>


### The '{model}.objects.all().first()' method
To query & fetch <u>the first record</u> from the database using the 'objects' manager.
<small>[Commit Link]()</small>


### The '{model}.objects.all().last()' method
To query & fetch <u>the last record</u> from the database using the 'objects' manager.
<small>[Commit Link]()</small>


### The '{model}.objects.all().[0:4]' method
To query & fetch <u>the first five records</u> from the database using the indexing into django queryset.
<small>[Commit Link]()</small>


### The '{model}.objects.create()' method
Create <u>a new record</u> using the '<b>.create()</b>' method. The model fields will be passed as kwargs inside this method.
<small>[Commit Link]()</small>


### The '{model}.objects.get_or_create()' method
First perform a lookup into the DB, if a record is not found, then only create <u>a new record</u> using the '<b>.get_or_create()</b>' method. The model fields will be passed as kwargs inside this method.
<small>[Commit Link]()</small>


### The '{model}.objects.count()' method
Count <u>the total number of record(s)</u> using the '<b>.count()</b>' method.
<small>[Commit Link]()</small>


### Working With The Foreign Keys
If a table contains any foreign relationship with another table, and we want to insert a new record using the Django ORM, then we are required to first fetch the instance of the record from that foreign table, after that, we can insert <u>the instance itself as foreign field value</u> into the main table.
<small>[Commit Link]()</small>


### The '.filter()' method
The '<b>.filter()</b>' method returns a queryset (_list_) of records which meet the condition that is passed as kwarg-value inside the method. 
<small>[Commit Link]()</small>


### The '.get()' method
The '<b>.get()</b>' method returns a class instance of a record which meet the condition that is passed as kwarg-value inside the method. 
<br/>
<small><b>Note:</b> If a record contains any foreign key data, then that can be called without executing another ORM query, since they (_foreign keys_) are being fetched at the first ORM query execution.</small>
<small>[Commit Link]()</small>


### Querying Reverse Relation in Django ORM
#### Method-1: Using '{model}_set' Manager
If a model has a <b>ForeignKey</b>, and we want to access the instances of that foreign-key-model, then we can use default <b>Manager</b> called `{model}_set`.
<br/>
<small><b>ie.</b> If we want to retrieve all the records of rating for a specific restaurant, just by using the restaurant instance, where the rating table has restaurant as foreign-key, we will use the following ORM query:
<br/>
> restaurant = Restaurant.objects.first() <br/>
ratings = restaurant.rating_set.all() <br/>
print(ratings)
</small>

<small>[Commit Link]()</small>

#### Method-2: Using Custom Name for Reverse Manager
Instead of using the default `{model}_set` manager, for executing reverse query, we can use a custom reverse manager name by defining an extra kwarg in the model-field param.
<br/>
<small>
<b>ie.</b> In the 'Rating' table, where the restaurant-field is defined, add another extra kwargs like the following:
<br/>
> restaurant = models.ForeignKey(Restaurant, on_delete=CASCADE, related_name='ratings') <br/><br/>
Execute the commands: <br/>
python manage.py makegrations <br/>
python manage.py migrate <br/><br/>
restaurant = Restaurant.objects.first() <br/>
ratings = restaurant.ratings.all() <br/>
print(ratings)
</small>

<small>[Commit Link]()</small>