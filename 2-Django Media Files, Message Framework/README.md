# Integration of Media Files In Both Django FBV & CBV Views

### 🎯Objectives

1. ✅Create Model-Forms in Django function-based view (FBV) for the CRUD operations.
2. ✅Integrate media files to serve in the development server.
3. ✅Integrate Django's message framework.
4. Handle CRUD operations using class-based view (CBV) & serve the media files.

\*\* The initial setup of a Django Project w/ frontend is demonstrated inside another folder | Link

<hr/>

### 📌Objective-1, 2, 3

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
6. [**Django Message Framework**] I imported the `messages` from `django.contrib` package. After any successful form operations, I defined the `message.success(request=request, message='.....')`. The message framework is passed as an iteratble in the template, thus I used the _for-loop_ template tag to iterate the message to the template.

#### 🤦‍♀️Bug Fix

**The Mistake:** While implementing the product updation functionality, I thought the modelForm only required the `request.POST` method to validate. While configuring the **Django Message Framework**, I deleted all the pictures associated with the products. <br/> While updating the pictures (_adding new image_) of each product, I accidently tried to upload an image whose length of the filename exceeded 100 characters. Thus the Django program crashes displaying the data could not be changed since it's not validated.<br/>
**The Solution:** I thought the `request.FILES` need to be validated along with `request.POST` data. After defining the files inside the "**ProductForm(...., files=request.FILES)**", I tried to re-submit the form with the same image. Finally I got a proper error message in the Django form without getting crashed.

    > Ensure this filename has at most 100 characters (it has 117).

### 🛠️ File Structure Refactorization - Separate the FBV & CBV

1. In order to segregate the class-based views & function-based views, initially I create a folders for **views** & inside of that I created 2 different views **views_fbv.py** & **views_cbv.py** files.
2. Similarly, I separated the urls for CBVs & FBVs in the **urls** folder, inside the 2 files naming **urls_fbv.py** & **urls_cbv.py**.
3. Also, I separated the template folders accordingly, creating **cbv_templates** & **fbv_templates**.
4. Finally, I re-pointed the file paths respectively throughout the **views**, **urls** & **templates** files.

<hr>

### 📌Objective-4

1. [**ListView**] I created a class named **ProductListView**, where I defined the `model` which Django will process the data from, the `template_name` attribute & the `context_object_name`. This is enough to view all the product records to the template.
    - In the template `list-product.html`, we can display the product records by iterating over the object-name which is defined in the `context_object_name`. 