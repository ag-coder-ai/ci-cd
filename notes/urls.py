from django.urls import path
from .views import home,navbar

urlpatterns = [

    path('', home, name='home'),
    path('nav/', navbar, name='navbar'),

]