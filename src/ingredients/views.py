from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Ingredient
from .forms import CreateIngredientForm
from recipe_project.views import profile_absolute_url

# Create your views here.

class IngredientListView(ListView):
    model = Ingredient
    template_name = 'ingredients/main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        profile_url = profile_absolute_url(self.request)

        context["profile_url"] = profile_url

        return context


class IngredientDetailView(DetailView):
    model = Ingredient
    template_name = 'ingredients/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        profile_url = profile_absolute_url(self.request)

        context["profile_url"] = profile_url

        return context
    
def create_ingredient_view(request):
    form = CreateIngredientForm( request.POST or None )

    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        ingredient_unit_type = request.POST.get('ingredient_unit_type')
        pic = request.FILES.get('pic')

        if not pic:
            pic = 'no_picture.jpg'
        else:
            print('Picture is chosen.')

        try:
            Ingredient.objects.create(
                name = name,
                price = price,
                ingredient_unit_type = ingredient_unit_type,
                pic = pic
            )

            return redirect('ingredients:create_ingredient_success')
        
        except:
            print('Something went wrong.')

    context = {
        'form': form
    }

    return render(request, 'ingredients/create_ingredient.html', context)

def create_ingredient_success_view(request):

    return render(request, 'ingredients/create_ingredient_success.html')