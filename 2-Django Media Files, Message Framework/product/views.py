from django.shortcuts import render


def productList(request):
    return render(
        request=request,
        template_name='product/index.html'
    )
