from django.urls import path
from employee.views import EmployeeView, EmployeeDetailView


urlpatterns = [
    path('', view=EmployeeView.as_view()),
    path('<int:pk>/', view=EmployeeDetailView.as_view())
]
