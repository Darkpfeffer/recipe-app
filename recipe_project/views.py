from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterUserForm
from users.models import User, UserAuth

def login_view(request):
    if request.user.is_authenticated:
        return redirect('recipes:home')

    redirect_request = request.GET.get("next")
    error_message = None
    redirect_to_page = False

    if redirect_request:
        redirect_to_page = True

    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                if not redirect_to_page:
                    return redirect('success')
                else:
                    return redirect(redirect_request)
        
        else:
            error_message = 'Something went wrong.'
    
    context = {
        'form': form,
        'error_message': error_message
    }

    return render(request, 'auth/login.html', context)

def register_view(request):
    if request.user.is_authenticated:
        return redirect('recipes:home')
    
    error_message = None

    form = RegisterUserForm(request.POST or None)

    if request.method == 'POST':
        form = RegisterUserForm(request.POST, request.FILES)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            profile_pic = form.cleaned_data.get('profile_pic')

           

            try:
                User.objects.get(user_info__username = username)
                error_message = "Username is already taken."
            except:
                user = UserAuth.objects.create_user(username, email, password)

                if user is not None:
                    User.objects.create(
                        user_info = user,
                        profile_pic = profile_pic
                    )

                    return redirect('login')
                    
                else:
                    error_message = "Something went wrong."

    context =  {
        'form': form,
        'error_message': error_message,
    }

    return render( request, 'auth/register.html', context)        

def logout_view(request):
    logout(request)
    return redirect('success')

def success_view(request):
    context = {
        'profile_url': profile_absolute_url(request)
    }
    return render(request, 'auth/success.html', context)

def profile_absolute_url(request):
    profile = None

    try:
        profile = User.objects.get(user_info__id = request.user.id).id
    except:
        print('User is not logged in.')
    return reverse('users:profile', kwargs={'pk': profile})

def user_absolute_url(request):
    user = None

    try:
        user = request.user.id
    except:
        print('User is not found')

    return reverse('users:edit_email', kwargs={'pk': user})