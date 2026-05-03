from django.shortcuts import render


def productIndex(request):
    context = {}
    return render(
        request=request,
        template_name='product/index.html',
        context=context
    )
