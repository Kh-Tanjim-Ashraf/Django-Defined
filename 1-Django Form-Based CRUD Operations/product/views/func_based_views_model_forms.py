from django.shortcuts import render
from forms.model_forms import ProductForm


def productIndex(request):
    return render(
        request=request,
        template_name='product/django_form_based_crud/index.html',
    )


def productCreateForm(request):
    return render(
        request=request,

    )
