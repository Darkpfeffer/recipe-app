from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from recipe_project.views import profile_absolute_url, user_absolute_url
from django.contrib.auth.models import User as UserAuth
from .models import User
# Create your views here.

class EditEmailView(LoginRequiredMixin, UpdateView):
    model = UserAuth
    fields = ['email']
    template_name = 'users/edit_email.html'
    success_url = reverse_lazy('users:edit_email_success')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user

        context["user"] = user

        return context
    
def edit_email_success_view(request):

    return render(request, 'users/edit_email_success.html')
class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user

        profile_url = profile_absolute_url(self.request)

        change_email_url = user_absolute_url(self.request)

        context["change_email_url"] = change_email_url

        context["user"] = user

        context["profile_url"] = profile_url

        return context
