from django.shortcuts import render
from django.views.generic import DetailView
from .models import User
# Create your views here.

class ProfileDetailView(DetailView):
    model = User
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user

        context["user"] = user

        return context