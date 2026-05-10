# Demostration of Form-based CRUD Operations

### 🎯Objectives

1. ✅ Create basic HTML forms for CRUD operations.
2. ✅ Create Model-Forms in Django for the same operations.
3. Create Django Generic Forms for the same operations. <br/>
   <small>NB: Use separate URL-blocks while demonstrating CRUD operations in different types forms.</small>

\*\* The initial setup of a Django Project w/ frontend is demonstrated inside another folder | Link

<hr/>

### 📌Objective-1

1. After the initial setup, I've created a separate sub-folder "_forms_" in "_templates_" dir for HTML-based forms. There I've created a '**product-form.html**' file. <br/>
   This form is included into the "**create-product.html**" file using the <u>_include_</u> tag of Django template.
2. [**Create Record**] Retrieve the input values sent from the frontend form into the create-function & create a new record inside the "Product" table. Then navigate the user to the product-list page.
3. [**Update Record**] Create a product detail page named "**detail-product.html**" file & include the product-form into this page. <br/>
4. The URL path will contain a path parameter in order to pass the product-id into the backend function. After retrieving the product-detail instance using the product-id, we passes that value into the frontend page through context. <br/>
5. _But the caveat here is_, the information we get from the backend into the frontend (**detail-product.html**), we are required to pass that same product-detail information into the form template (**product-form.html**) since we included that inside this page. <br/>
   Luckily, we can pass further information into an included-html-part using the "_with_" keyword along with assinging the value with a key.
   An example is given below:

   > {% include 'forms/product-form.html' with prod=product %}

   The product information passed inside the **product-form.html** page can be retrieved using the "**prod**" key & store them inside the "_value_" attr of input fields.

6. Make modification in product detail, then send a post request to the backend function, it receives the data & update the product instance accordingly that it retrieved earlier (_for sending the info the the detail-page for populating input field_). Finally, redirect the user to the product list page.
7. [**Delete Record**] Like the product detail & update functionality, I create a delete-confirmation page named "**delete-product.html**" file. Rendered that page with product detail information. The product will be deleted from the DB if the user clicks the delete button & navigate the user to the product-list page.

<hr/>

### 🛠️File Structure Refactorization

I wanted to demonstrate the CRUD operations based upon both the function & class-based views along with the HTML-form, Django-model form & Django-generic form. Thus I created a "**views**" folder inside the "product" app. <br/>
I moved the previous views file & renamed it as "**func_based_views_html_forms.py**". Also created another view file named "**func_based_views_model_forms.py**" to separate the CRUD operations on Django-model-based forms.<br/>
The _imports_ inside the views & urls files have changed accordingly. <br/>
I separated the HTML-form & Django-form based templates into two separate folders named "**html_based_crud**" & "**django_form_based_crud**".
I segregated the urls accordingly for the html-form-based & Django-form-based CRUD operations.

<hr/>

### 📌Objective-2

1. I created a form-class file named "**model_forms.py**" for model-form (_ProductForm_). It's a simple model based form, where I included all the fields of "**Product**" model using the `__all__` string attr.
2. Inside the model-form-based view ("**func_based_views_model_forms.py**"), I created the product-list page again, because I didn't want to make confusion between the named-URLs of two different form-based approaches.
3. [**Create Record**] For the create operation, initially, instantiate the model-form (_ProductForm_), thus an empty form appears whenever a user makes a `Get` request.
4. After getting the `Post` request, I passed the request-data straight inside the model-form (_ProductForm_) as data, check if the data is valid using the `is_valid()` function. If no error occured, save teh data-form to create the record inside the DB. Finally redirect the user to the product-list page.
5. [**Update Record**] Initially, get the product-record by it's id, then instantiate the model-form (_ProductForm_) with the product data by passing them through `instance` param of that form. So that, any user makes the `Get` request will get a page loaded with the form & data.
6. Make antoher if-condition block to handle the `Post` request. There, I passed the request-data into the model-form (_ProductForm_) in order to execute the form validation using the `is_valid()` function.
7. If no error occured, I passed the request-data again along with product-instance record into the model-form (_ProductForm_) object. Finally execute the `.save()` function to commit the change into the DB.
8. [**Delete Record**] Initially I retrieved the product object using it's id, so that the user can get confirmed before deleting the record. It's for the `Get` request. I added a form with **submit** button so that if the user confimed to delete the record then the backend can process the request based on `request.method == "POST"` method. Finally redirect the user to the product-list page.

<hr/>

### 🛠️File Structure Refactorization

1. Created a separate view named "**func_based_views_dj_generic_forms.py**" for defining function-based-views integrated with Django generic forms.
2. Created a different template sub folder named "**django_generic_form_based_crud**" for the HTML files.
3. Separated the urls of Django generic forms inside the same "**urls.py**" file.

<hr/>

### 📌Objective-3

1. Like the previous processes, we are required to have an index file ("**index.html**") which shows the product records as list. <br/>
   The file path is: _product/django_generic_form_based_crud/index.html_
2. I created a form inside the "**generic_forms.py**" file, where I created a Django form class (_ProductFormGen_). In this form class, I inherited the _forms.Form_ module by defining the import as `from django import forms`. <br/>
   This provides me a standard Django form, with no model attached to it. Thus I need to manually define each field which I want to show in the frontend form.
3. [**Create Record**] I created a basic view to propagate the standard Django form (_ProductFormGen_) earlier I created inside the "**generic_forms.py**" file. The view function is currently build to handle the get request only, since I will test & implement different levels of validation inside the form along with it's fields.
   - After implementing different form validations & testing, I defined the product create functionality into the "**productCreate()**" function. <br/>
     Since, this form is not associated with any Django model, we are required to extract each fields user-input through invoking the form's **cleaned_data** dictionary which is containing all the data as key-value pairs. <br/>
     Finally, I passed thse values as params of the "**create()**" method of the "**Product**" class.

     > Product.objects.create(name=\<value\>, quantity=\<value\>, price=\<value\>)

4. [**Form Validations**] Inside the "**ProductFormGen()**" class, I have created 3 types of form validations:
   - [**Field-level constraints - Validators**]: By using the "_validators_" param on single form fields, we can perform simple validation checks. For this, I've used "_MinValueValidator()_" in the "_quantity_" & "_price_" fields to prevent negative inputs.
   - [**Field-level constraints - clean_\<fieldname\>**]: For implementing more complex validation logic in individual field, we can define a method containing "_clean\_\<fieldname\>(self)_" inside the Django form class. We implement such validations in both the "_quantity_" & "_price_" fields. But it's required to **<u>return the data</u>** from these clean methods.
   - [**Form-level constraints - clean() method**]: If we want to build validation logic where two or more form fields need to be compared, then we define the "_clean(self)_" method. This cross validation is performed on the entire form. It's also required to **<u>return the data</u>** from the method.
5. [**Update Record**] Initially defined the function "**productUpdate()**" to handle the **GET** request, where an empty unbound Django form is initialized & passed to the Django's **Template Engine** to render in the template. <br/>
   [_Conditional Separation_]: A user will submit a form for updation operation, thus the **GET** & **POST** requests are conditionally separated based on _request.method_. <br/>
   [_'initial' param - GET request_]: Unlike the Django model form, record-object is passed through the '_instance_' param to display the record in the template. But for the standard forms of Django we are required to use the '_initial_' param.
   - For this, we need to create a dictionary ensuring the keys are equivalent to the form fields to map the record objects correctly.
   - Then pass the mapped dictionary to the '_initial_' param of the form.

   [_POST request_]: Since we defined some manual validations, to execute those operations, we are required to pass the user-inputs as <u>**request.POST**</u> through the form (_ProductFormGen()_) class. After the form gets validated, store each user-inputs from the <u>**cleaned_data**</u> dictionary & replace the field value of the previously retrieved product object. <br/>
   Finally to reflect the updated value into the DB, we are required to execute the `.save()` method on the product-record obejct. After successfully saved the update into the DB, redurect the user using the `redirect(\<named_url_of_next_page\>)` method.

## ✨Concept Of Workflow

NB: Before making any functionality which requires a separate HTML page, I start with a minimal HTML page, then I create the view function to just return the newly created page. Lastly I plug the URL path to that view function in order to access the page from browser. Then I start building the logic & the HTML page simultaneously.
