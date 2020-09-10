from django.urls import path, include
from .views import home, my_logout
from core import urls as core_urls

urlpatterns = [
    path('', home, name='home'),
    path('logout/', my_logout, name="logout"),
    path('core', include(core_urls))
]