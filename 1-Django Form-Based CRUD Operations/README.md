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

## ✨Concept Of Workflow

NB: Before making any functionality which requires a separate HTML page, I start with a minimal HTML page, then I create the view function to just return the newly created page. Lastly I plug the URL path to that view function in order to access the page from browser. Then I start building the logic & the HTML page simultaneously.
