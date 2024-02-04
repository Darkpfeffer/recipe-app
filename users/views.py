from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from recipe_project.views import profile_absolute_url, user_absolute_url
from django.contrib.auth.models import User as UserAuth
from recipes.models import Recipe
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

        profile = User.objects.get(user_info = user)

        context["profile"] = profile

        return context
    
def edit_email_success_view(request):

    profile_url = profile_absolute_url(request)

    context = {
        "profile_url": profile_url
    }

    return render(request, 'users/edit_email_success.html', context)
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

def delete_user_view(request, pk):
    user = User.objects.get(id = pk)
    userAuth = UserAuth.objects.get(id = user.user_info.id)
    recipe = Recipe.objects.filter(creator = user)

    if request.method == 'POST':
        user_confirmation = request.POST.get('delete-checkbox')
        if user_confirmation:
            for created_recipe in recipe.all():
                created_recipe.creator = None
                created_recipe.save()

            user.delete() 
            userAuth.delete()  

        return redirect('recipes:home')         

    if userAuth == request.user:
        return render(request, 'users/delete_user.html')
    else:
        return redirect('/profile/'+ str(user.id))