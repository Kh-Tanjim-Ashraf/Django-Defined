from django import forms


class ProductFormGen(forms.Form):
    name = forms.CharField(max_length=200)
    quantity = forms.IntegerField()
    price = forms.FloatField()

    