from django.urls import path
from company.views import CompanyView, CompanyDetailView


urlpatterns = [
    path('', view=CompanyView.as_view()),
    path('<int:pk>/', view=CompanyDetailView.as_view()),
]
