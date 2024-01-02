from django.urls import path, reverse_lazy, include
from .views import ProfileDetailView, EditEmailView, edit_email_success_view
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('profile/<pk>', ProfileDetailView.as_view(), name='profile'),
    path('profile/update', include('django.contrib.auth.urls')),
    path('profile/update/password', auth_views.PasswordChangeView.as_view(
        success_url = reverse_lazy('users:password_change_done'),
        template_name = 'users/edit_password.html'), 
        name='edit_password'
    ),
    path('profile/<pk>/update/email', EditEmailView.as_view(), name='edit_email'),
    path('profile/update/email/success', edit_email_success_view, name='edit_email_success')
]