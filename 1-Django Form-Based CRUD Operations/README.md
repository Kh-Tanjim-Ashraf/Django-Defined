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
