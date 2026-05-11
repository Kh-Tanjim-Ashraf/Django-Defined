# Integration of Media Files In Both Django FBV & CBV Views

### 🎯Objectives

2. Create Model-Forms in Django function-based view (FBV) for the CRUD operations.
3. Integrate media files to serve in the development server.
4. Handle CRUD operations using class-based view (CBV) & serve the media files.

\*\* The initial setup of a Django Project w/ frontend is demonstrated inside another folder | Link

<hr/>

### 📌Objective-1

1. Initialize the basic setup for the Django development server till showing **<u>a product list page</u>** in the frontend.
2. [**Create Record**] A Django model form class (**ProductForm()**) is created inside the "_product/forms/product_model_form.py_" file. Then I created the "**productCreate()**" function to handle the product-create functionality. <br/>
   Finally, after the product-creation operation gets completed the user will be redirected to the product-list page.
3. [**Update Record**] For the updation of record, data binding to the form is crucial regardless of a `GET` or `POST` request. Retrieved the specific product in the view function (**productUpdate()**) using the product id passed in through the URL parameter.
   - <u>For the `GET` request</u>, bind the **product** object into the form "**ProductForm(instance=product)**" thorugh the instance param.
   - <u>For the `POST` request</u>, bind the **product** object along with the user-input data as **ProductForm(data=request.POST, instance=product)** considering the usage of '_data_' & '_instance_' param accordingly.
4. [**Delete Record**] Initially retrieve the product record using id value passed through URL parameter. That record is passed to the **Template Engine** in the `GET` request to render it to the template so that the user can ensure about the product that is going to be deleted. A simple form with a _submit_ button is placed beneath the product information to make a `POST` request to delete the record from the DB. After a successful deletion of the product, the user will be redirected to the product-list page.
