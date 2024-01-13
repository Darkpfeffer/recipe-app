from django import forms

class RegisterUserForm(forms.Form):
    username = forms.CharField(max_length=120)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()
    profile_pic = forms.ImageField(required=False)