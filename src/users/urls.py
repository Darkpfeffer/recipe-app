from django.urls import path
from .views import ProfileDetailView

app_name = 'users'

urlpatterns = [
    path('profile/<pk>', ProfileDetailView.as_view(), name='profile')
]