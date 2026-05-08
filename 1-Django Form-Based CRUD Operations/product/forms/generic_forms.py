from django import forms
from django.core.validators import MinValueValidator


class ProductFormGen(forms.Form):
    name = forms.CharField(max_length=200)
    quantity = forms.IntegerField(validators=[MinValueValidator(0, message="Quantity could not be negative")]) # Basic Field-level Validator
    price = forms.FloatField(validators=[MinValueValidator(1, message="Price could not be negative")]) # Basic Field-level Validator

    def clean_name(self):
        data = self.cleaned_data.get('name')
        data = data.strip() # Removes the leading/trailing whitespaces

        # Product name cannot contain the word "test"
        if 'test' in data.lower():
            raise forms.ValidationError("Product name cannot contain the word 'test'")
        return data
    
    def clean_quantity(self):
        data = self.cleaned_data.get('quantity')
        # Check bulk order confirmation from WM
        if data > 500:
            # Perform other business logic
            raise forms.ValidationError(f"Product quantity {data} requires approval of warehouse manager!")
        return data

    def clean_price(self):
        data = self.cleaned_data.get('price')
        # Check the price threshold
        if data > 10000:
            # Perform other business logic
            raise forms.ValidationError(f"Price of BDT {data} requires retail manager's approval!")
        return data
    
    def clean(self):
        cleaned_data = super().clean()
        quantity = self.cleaned_data.get('quantity')
        price = self.cleaned_data.get('price')
        # If the price is very high, the quantity should be low to prevent stock error
        if price and quantity:
            total_stock_value = price*quantity
            if total_stock_value > 50000:
                raise forms.ValidationError(f"Total value {total_stock_value} exceeds warehouse limits!")
        return cleaned_data