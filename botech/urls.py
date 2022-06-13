from django.urls import path
from .views import home

app_name ='botech'

urlpatterns = [
    path('home', home, name = 'home'),
]