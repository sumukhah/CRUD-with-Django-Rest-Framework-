from django import forms
from allauth.account.forms import SignupForm
from .models import User


class CustomAdminCreationForm(SignupForm):
    name = forms.CharField(max_length=25, required=True)
    email = forms.CharField(max_length=50, required=True)

    def signup(self, request, user):
        user.name = self.cleaned_data.get['name']
        user.email = self.cleaned_data.get('email')
        user.save()
        return user
