from django import forms
from django.contrib.auth import get_user_model

from .models import Projects


from django import forms
from django.contrib.auth import get_user_model
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profession','headline','slogan','location_city','location_state','location_country']



class ProjectsForm(forms.ModelForm):
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d'],  # Adjust to your desired format
    )
    end_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d'],  # Adjust to your desired format
    )

    class Meta:
        model = Projects
        fields = ['projects_title', 'company', 'start_date', 'end_date', 'description']