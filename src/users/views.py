from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from recipe_project.views import profile_absolute_url
from django.contrib.auth.models import User as UserAuth
from .models import User
# Create your views here.

class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user

        profile_url = profile_absolute_url(self.request)

        context["user"] = user

        context["profile_url"] = profile_url

        return context
