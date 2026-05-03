# Demostration of Form-based CRUD Operations

### Objectives

1. ✅ Create basic HTML forms for CRUD operations.
2. Create Model-Forms in Django for the same operations.
3. Create Django Generic Forms for the same operations. <br/>
   <small>NB: Use separate URL-blocks while demonstrating CRUD operations in different types forms.</small>

\*\* The initial setup of a Django Project w/ frontend is demonstrated inside another folder | Link

<hr/>

### Objective-1

1. After the initial setup, I've created a separate sub-folder "_forms_" in "_templates_" dir for HTML-based forms. There I've created a '**product-form.html**' file. <br/>
   This form is included into the "**create-product.html**" file using the <u>_include_</u> tag of Django template.
2. [**Create Record**] Retrieve the input values sent from the frontend form into the create-function & create a new record inside the "Product" table.
3. [**Update Record**] Create a product detail page named "**detail-product.html**" file & include the product-form into this page. <br/>
4. The URL path will contain a path parameter in order to pass the product-id into the backend function. After retrieving the product-detail instance using the product-id, we passes that value into the frontend page through context. <br/>
5. _But the caveat here is_, the information we get from the backend into the frontend (**detail-product.html**), we are required to pass that same product-detail information into the form template (**product-form.html**) since we included that inside this page. <br/>
Luckily, we can pass further information into an included-html-part using the "_with_" keyword along with assinging the value with a key.
An example is given below:

   > {% include 'forms/product-form.html' with prod=product %}

   The product information passed inside the **product-form.html** page can be retrieved using the "**prod**" key & store them inside the "_value_" attr of input fields.
6. Make modification in product detail, then send a post request to the backend function, it receives the data & update the product instance accordingly that it retrieved earlier (_for sending the info the the detail-page for populating input field_). Finally, redirect the user to the product list page.


<!-- Concept Of Workflow -->
NB: Before making any functionality which requires a separate HTML page, I started with a minimal HTML page, then I create the view function to just return the newly created page. Lastly I plug the URL path to that view function in order to access the page from browser. Then I start building the logic & the HTML page simultaneously.