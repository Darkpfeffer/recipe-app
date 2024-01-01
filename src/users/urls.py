from django.urls import path, reverse_lazy, include
from .views import ProfileDetailView
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('profile/<pk>', ProfileDetailView.as_view(), name='profile'),
    path('profile/update', include('django.contrib.auth.urls')),
    path('profile/update/password', auth_views.PasswordChangeView.as_view(success_url = reverse_lazy('users:password_change_done')), name='edit_password')
]