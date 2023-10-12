from django import forms
from .models import UserBase

class RegistrationForm(forms.ModelForm):
    user_name = forms.CharField(label='Enter Username', min_length=4,
                                max_length=50, help_text='Required')
    email = fprms
