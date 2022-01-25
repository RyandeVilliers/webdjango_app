from django.urls import path

# Use method in views module
# '' means root
# Path is called index
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about', views.about, name = 'about')
]