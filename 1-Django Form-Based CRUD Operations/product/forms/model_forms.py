from django.forms import ModelForm
from product.models import Product

class ProductForm(ModelForm):
    class Meta:
        model=Product
        fields='__all__' # This string will get all the fields from the model; otherwise need to use a list of model fields name
