from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .validators import validate_gmail_email

class UserAdminCreationForm(UserCreationForm):
    """
    A Custom form for creating new users.
    """
    email = forms.EmailField(validators=[validate_gmail_email])

    class Meta:
        model = get_user_model()
        fields = ['email']