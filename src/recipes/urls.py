#import
from django.urls import path
from .views import home

#defining URLs and variables
app_name = 'recipes'

urlpatterns = [
    path('', home)
]