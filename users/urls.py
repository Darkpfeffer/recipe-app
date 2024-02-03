from django.urls import path, reverse_lazy, include
from .views import ProfileDetailView, EditEmailView, edit_email_success_view, \
delete_user_view
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('<pk>', ProfileDetailView.as_view(), name='profile'),
    path('update', include('django.contrib.auth.urls')),
    path('update/password', auth_views.PasswordChangeView.as_view(
        success_url = reverse_lazy('users:password_change_done'),
        template_name = 'users/edit_password.html'), 
        name='edit_password'
    ),
    path('<pk>/update/email', EditEmailView.as_view(), name='edit_email'),
    path('update/email/success', edit_email_success_view, name='edit_email_success'),
    path('<pk>/delete/', delete_user_view, name='delete_user')
]