# Integration of Media Files In Both Django FBV & CBV Views

### 🎯Objectives

2. ✅Create Model-Forms in Django function-based view (FBV) for the CRUD operations.
3. ✅Integrate media files to serve in the development server.
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
5. [**Configure Media Files Handling**] To store media files during development, firstly, we need to make sure that the "**Product**" model has an <u>image field</u> to handle image files. <br/>
   - We need to define the "**MEDIA_URL**" & "**MEDIA_ROOT**" variables as configs inside the "**settings.py**" file.
     - **MEDIA_URL:** It's used to define URL-path inside the browser
     - **MEDIA_ROOT:** It's used to define host machine's local directory path.
   - Later I've joined the <u>static file serving config</u> in the project's main "**urls.py**" file to ensure that this project can handle inputs of the media files. <br/>
     <small>_NB: At this stage, we can locally store images of product through the default admin panel of Django_</small>
   - Configure the <u>product creation form</u> to submit the associate product image to the backend function. Simply used an `<img>` field & include `enctype='multipart/form-data'` in the HTML form. <br/>
     In the backend function (**productCreate()**), include the `request.FILES` as another parameter in the Django modelForm **ProductForm(....., files=request.FILES)**. After that, it'll be able to store the media files into the local storage of this project. In addition to to this, it'll store the path of the storage (_as string_) into the DB.
   - Similar to the configuration of product creation form functionality, the <u>update product form</u> also got modified to update the product image along with other records.
   - I also updated the <u>prodcut deletion page</u> to display product image before deleting the record.
   - To <u>display images in the templates</u>, we need to use the `<img>` tag & define the image-path-string `{{ product.image.url }}` to the _src_ attribute.
