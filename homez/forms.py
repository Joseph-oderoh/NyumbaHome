from django import forms
from django.contrib.auth.models import User
from .models import Profile, Nyumbani

class NyumbaniForm(forms.ModelForm):
    class Meta:
        model = Nyumbani
        exclude = ('admin',)





class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email')

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'neighbourhood')

