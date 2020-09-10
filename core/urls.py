from django.urls import path
from .views import personList, newPerson, personUpdate, personDelete

urlpatterns = [
    path('', personList, name='personList'),
    path('new', newPerson, name='newPerson'),
    path('update/<int:id>/', personUpdate, name='personUpdate'),
    path('delete/<int:id>/', personDelete, name='personDelete'),
]
