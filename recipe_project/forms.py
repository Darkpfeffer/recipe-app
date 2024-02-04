from django import forms
from PIL import Image
from django.core.exceptions import ValidationError

def validate_image(file):
    try:
        Image.open(file)
        return file
    except:
        raise ValidationError("File is not supported")

class RegisterUserForm(forms.Form):
    username = forms.CharField(max_length=120)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()
    profile_pic = forms.ImageField(required=False, validators=[validate_image])