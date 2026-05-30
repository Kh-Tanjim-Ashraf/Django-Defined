from django import forms
from django.forms import ModelForm
from product.models import Product
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator


class ProductForm(ModelForm):

    # Reusable core validator
    price = forms.DecimalField(required=False, validators=[MinValueValidator(1, message="Price cannot be negative!")])
    
    class Meta:
        model = Product
        fields = '__all__'

    """
    Note: Similar to Django generic form, we can apply any of the 3 levels of validations in Django model form: 
        1. Field-level validation (clean_<fieldname>).
        2. Form-level validation (clean).
        3. Reusable core validators.
    """

    # Field-Level Validation
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if 'test' in name:
            raise ValidationError('Product name cannot contain "Test"!')
        return name
    
    # Form-Level Validation; Basically used form cross-field validation
    def clean(self):
        cleaned_data = super().clean()
        name = self.cleaned_data.get('name')
        quantity = self.cleaned_data.get('quantity')
        price = self.cleaned_data.get('price')

        if quantity > 1000 and price > 9999:
            raise ValidationError(f'Stock limit {quantity} & price {price} requires manager\'s permission')
        return cleaned_data