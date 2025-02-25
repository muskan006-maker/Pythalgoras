from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "name", "location", "opening_paragraph",
            "degree_1", "institution_1", "year_completed_1",
            "degree_2", "institution_2", "year_completed_2",
            "degree_3", "institution_3", "year_completed_3",
            "job_title_1", "company_1", "start_date_1", "end_date_1", "job_description_1",
            "job_title_2", "company_2", "start_date_2", "end_date_2", "job_description_2",
            "job_title_3", "company_3", "start_date_3", "end_date_3", "job_description_3",
            "project_title_1", "project_description_1", "project_link_1",
            "project_title_2", "project_description_2", "project_link_2",
            "project_title_3", "project_description_3", "project_link_3",
        ]
