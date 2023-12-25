from django.urls import path
from .views import home
from .views import contacts
from .views import aboutUs
from .views import typography

urlpatterns = [
    path('', home, name='home.html'),
    path('contacts.html/', contacts, name='contacts'),
    path('about-us.html/', aboutUs, name='about-us'),
    path('typography.html/', typography, name='typography'),
]
