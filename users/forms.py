from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

# Create User Form
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'role', 'password1', 'password2']

# Edit User Form (Superadmin can edit all fields)
class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'role',]

    def __init__(self, *args, **kwargs):
        super(EditUserForm, self).__init__(*args, **kwargs)
        self.fields['role'].choices = User.ROLE_CHOICES
