# Django Polling App

I am building this polling app according to the instructions provided in the <a href="https://docs.djangoproject.com/en/6.0/intro/">official Django documentation</a>. The purpose of building this app is to get a better knowledge of Django from it's official site instead of other sources in the internet. I will try to include additional information where I find it difficult to understand any topic.

## <a href="https://docs.djangoproject.com/en/6.0/intro/tutorial01/">Tutorial-1</a>

#### <u>Learning Outcomes</u>

1. How to setup Python's virtual environment for a Django project.
2. Initialize a Django project & understand the file structure of the project.
3. Create a new app (battery) named "Polls".
4. Create a basic view (_where business logic resides_) for the app inside the app directory.
5. Define a url path for that view so that the request can route to the appropriate view.
6. Use _include()_ in the parent url-config file, thus any request meant for the "Polls" app will be routed to that app's url-config file for further processing.

#### <u>Development Flow</u>

1. Setup & activate a virtual environment of python using the following commands.

   > python -m venv env <br/>
   > source env/Scripts/activate

2. Initialize a Django project which will create a file structure of the project's config file.

   > django-admin startproject pollingAppClassic .

   NB: The dot (.) at the end of the command ensures a flat scaffolding of the project, meaning the project folder will not create a sub-folder of the same name (_pollingAppClassic_) for the project's configuration. Instead the config folder will be created in the project's root directory along with the **manage.py** file.

   The file structure includes the following:
   - | pollingAppClassic/
     - | \_\_pycache\_\_/
     - | \_\_init\_\_.py
     - | asgi.py
     - | settings.py
     - | urls.py
     - | wsgi.py
   - | manage.py
   - | env/

3. Create a new app (**Polls**) inside the project using the following command.

   > django-admin startapp polls

   Any kind of business logic related to polls functionality will reside inside the **views.py** file.

   The app will contain the following file structure:
   - | polls/
     - | \_\_pycache\_\_/
     - | migrations/
     - | \_\_init\_\_.py
     - | admin.py
     - | apps.py
     - | models.py
     - | tests.py
     - | urls.py
     - | views.py

4. Create a simple view inside the **Polls** to return an **HTTP-response** to the user.

   > from django.http import HttpResponse <br/>
   > def index(request): <br/>
   > &emsp;&emsp;return HttpResponse("Hello world. You are at the polls index.")

5. To access this view in the browser, we'll define a URL inside the **urls.py** file of the **Polls** app.

   > from django.urls import path <br/>
   > from . import views <br/>
   > urlpatterns = [ <br/>
   >
   > > &emsp;path("", views.index), <br/>
   > > ]

6. Inside the parent **urls.py** file, add the **Poll** app urls using the **include()** function.

   > from django.contrib import admin <br/>
   > from django.urls import path, include <br/>
   > urlpatterns = [ <br>
   >
   > > &emsp;path('admin/', admin.site.urls), <br/>
   > > &emsp;path('polls/', include('polls.urls')), <br/>
   > > ]

   NB: When Django encounters **include()** function, it chops off whatever string is matched from the url-string of request, then sends the remaining string to the included URLconf (in this case, the URLconf of **Polls** app) for further processing.

7. Create Django's default database tables using the following command:

   > python manage.py migrate

8. Create two django-models named "**Question**" & "**Choice**" inside the **models.py** file in order to create database tables based on those models. <br/>
   <small>_NB: Each question might contain multiple choices, but a choice can only belong to a specific question. Thus this will be a One-To-Many relationship._</small>

   > from django.db import models <br/>

   > class Question (models.Model): <br/>
   > &emsp;question = models.CharField(max_length=200) <br/>
   > &emsp;pub_date = models.DateTimeField(verbose_name="Date Published")

   > class Choice(models.Model): <br/>
   > &emsp;question = models.ForeignKey(Question, on_delete=models.CASCADE) <br/>
   > &emsp;choice_text = models.CharField(max_length=200) <br/>
   > &emsp;votes = models.IntegerField(default=0)

   The class-attributes the **Question** & **Choice** model contain represents fields in database tables. In order to apply changes into the database, we are required to take the following steps: <br/>
   1. Define the **Polls** app inside the project's **settings.py** file.

      > INSTALLED_APPS [ <br/>
      >
      > > &emsp;'....', <br/>
      > > &emsp;'polls.apps.PollsConfig', <br/>
      > > ]

   2. Execute the **migrations** command to store the changes/creation of models to the local disk as **polls/migrations/0001_initial.py** file. This is a human-editable file, in case sometime we need to make some manual tweak before applying the changes into the database.

      > python manage.py makemigrations

   3. For applying those changes from the migrations files to the connected database, we need to execute the **migrate** command.

      > python manage.py migrate

9. Create the project's super user in order to use the **default admin panel** that is provided by Django out of the box. For that, use the following command:

   > python manage.py createsuperuser

   <small>NB: It'll prompt for the username, email & password for the super user (admin). Upon the successful creation of admin user & make the server up & running, we can access the admin panel by navigating to the url **127.0.0.1:8080**.</small>

   > python manage.py runserver 8080

10. We need to register the two models into the **admin.py** file, in order to view them inside the Django's default admin.

    > from django.contrib import admin <br/>
    > from .models import Question, Choice

    > admin.site.register(Question) <br/>
    > admin.site.register(Question)

    NB: Populate some data in those models, thus we can make some db operations using django-orm through the django's shell command.

11. While adding choices for the respective question from the admin panel, the select-from-dropbox was showing the question objects in a non-useful way. The question instances are showing as **Question Object (1)**, **Question Object (2)**.

    Thus for getting better representation of instance objects, we'll define the **\_\_str\_\_()** method inside the model classes. So the models will have the following definitions:

    > from django.db import models <br/>

    > class Question(models.Model): <br/>
    > &emsp;\*\*\* <br>
    > &emsp;def \_\_str\_\_(self): <br/>
    > &emsp;&emsp;return self.question

    > class Choice(models.Model): <br/>
    > &emsp;\*\*\* <br>
    > &emsp;def \_\_str\_\_(self): <br/>
    > &emsp;&emsp;return self.choice_text

12. In order to, check if a question was published a day ago (considering recent) as a boolean format result. Thus for this, I used the **timezone** module to find out the difference of time & compare it with each question-instance's pub_date.

    > from django.utils import timezone <br/>
    > def was_currently_published(self): <br/>
    > &emsp;self.pub_date >= timezone.now() - timezone.timedelta(days=1)

13. Each question have multiple choices, but each choice belongs to a specific question. Thus the question-choice has a **Many-To-One** relationship.

      In some scenarios, we need to get all the choices of a question. For such reverse query, we can use the **model_set** as "reverse relationship accesssor". For using this accessor, retrieve a question-instance first, then, use the **choice_set** attribute, then use the [<u>django-orm specific methods</u>](https://docs.djangoproject.com/en/6.0/ref/models/querysets/) (*.all(), .filter(), .exclude() etc.*) to make general db-operations on the **Choice** model. The following example will provide more clarity:

      > from .models import Question <br/>
      > q = Question.objects.get(id=1) <br/>
      > q.choice_set.all()
      
      <small>NB: It's related to the **related_name** attribute of class variables of a django model.</small>

      Otherwise, if we follow a brute force approach for retrieving all the choices of a specific question, then we need to retrieve the question instance first, then execute a *filter()* django-specific operation on the **Choice** model using the question instance to extract the choices connected with the specific question.
