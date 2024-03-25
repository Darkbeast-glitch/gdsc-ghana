from django.urls import path
from .views import HomePage, ContactUs
urlpatterns = [
    path('', HomePage, name='home'),
    path('contact/', ContactUs, name='contact')
]
