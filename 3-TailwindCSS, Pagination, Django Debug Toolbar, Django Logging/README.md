# Integrate TailwindCSS, Pagination, Debug Toolbar & Logging in Django

### 🎯Objectives

1.  ✅ Integrate pagination while displaying record list in web page.

    1.1# ✅ Insert 1000 product records into the product table to SQLite3, PostgreSQL & MySQL db using a Python script (_using the `runscript` command_).

    1.2# ❌ Integrate **PostgreSQL** & later **MySQL** database instead of **sqlite3** database, to view the architectural flaw known as "**Unpredictable Query Ordering**" caused by not using the **order_by()** method.

          1.2.1# ✅ Integrated PostgreSQL w/ Django app.

          1.2.2# ✅ Integrated MySQL w/ Django app.

          1.2.3# ❌ View the architectural flaw known as "Unpredictable Query Ordering".

    1.3# ✅ Implement form validation using Django's model form while `form.is_valid()` method is invoked.

2.  Integrate TailwindCSS in Django Full Stack Project.

    2.1# Extend a base template to multiple other templates.

    2.2# Use static template tag to serve static files on the website.

3.  Integrate Django Toolbar.
    3.1# Update the db structure, introducing <u>**One-To-One**</u>, <u>**One-To-Many**</u> & <u>**Many-To-Many**</u> relationships.

4.  Integrate Django Logging.

<hr/>

### 🛠️Initial File Structure

**Mental Model:** I want to implement the <u>pagination</u> in both the class-based & function-based views. I have only a single model (**Product**) in the entire project. Thus the _views_ & the _urls_ files will be separated inside the same battery (**Product**).

1. Created the boilerplate project setup using the following commands:

   > django-admin startproject core .

   > django-admin startapp product

2. Created _views_ & _urls_ subfolders inside the **Product** folder.

3. Renamed the provided **views.py** to **func_based_views.py** & moved that inside the views subfolder. Create another file **class_based_views.py** inside the same folder.

4. Similarly created 3 different url files inside the _urls_ subfolder. They are: **base_urls.py**, **fbv_urls.py**, **cbv_urls.py**.

5. Created a _templates_ folder in the project directory.

6. Created an **index.html** page inside the _templates_ folder for naviagting to **FBV** to **CBV**. Created two more similar pages inside the _fbv_ and _cbv_ subfolders to separate the CRUD operations.

7. In the **urls.py** inside project's system folder, include the **base_urls.py** along with the `namespace=ProductApplication`. On the other side, denote the `app_name="productApp"` inside the **base_urls.py** file.

8. In the **fbv_urls.py** file, add another url path as 'fbv/'. Similarly in the **cbv_urls.py** file, add another url path as 'cbv/'.

   **An idea of URL string pattern in the project:**

   > core.urls -> product.urls.base_urls -> ...fbv_urls <br/>
   > 'product/'&emsp;&emsp;-> 'fbv/' &emsp;&emsp;-> 'list/'

   > core.urls -> product.urls.base_urls -> ...cbv_urls <br/>
   > 'product/'&emsp;&emsp;-> 'cbv/' &emsp;&emsp;-> 'list/'
