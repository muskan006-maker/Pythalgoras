from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    # Link to Django's built-in User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Basic information
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True, null=True)
    opening_paragraph = models.TextField(blank=True, null=True)

    # Education (Up to 3 entries)
    degree_1 = models.CharField(max_length=255, blank=True, null=True)
    institution_1 = models.CharField(max_length=255, blank=True, null=True)
    year_completed_1 = models.IntegerField(blank=True, null=True)

    degree_2 = models.CharField(max_length=255, blank=True, null=True)
    institution_2 = models.CharField(max_length=255, blank=True, null=True)
    year_completed_2 = models.IntegerField(blank=True, null=True)

    degree_3 = models.CharField(max_length=255, blank=True, null=True)
    institution_3 = models.CharField(max_length=255, blank=True, null=True)
    year_completed_3 = models.IntegerField(blank=True, null=True)

    # Work Experience (Up to 3 entries)
    job_title_1 = models.CharField(max_length=255, blank=True, null=True)
    company_1 = models.CharField(max_length=255, blank=True, null=True)
    start_date_1 = models.DateField(blank=True, null=True)
    end_date_1 = models.DateField(blank=True, null=True)
    job_description_1 = models.TextField(blank=True, null=True)

    job_title_2 = models.CharField(max_length=255, blank=True, null=True)
    company_2 = models.CharField(max_length=255, blank=True, null=True)
    start_date_2 = models.DateField(blank=True, null=True)
    end_date_2 = models.DateField(blank=True, null=True)
    job_description_2 = models.TextField(blank=True, null=True)

    job_title_3 = models.CharField(max_length=255, blank=True, null=True)
    company_3 = models.CharField(max_length=255, blank=True, null=True)
    start_date_3 = models.DateField(blank=True, null=True)
    end_date_3 = models.DateField(blank=True, null=True)
    job_description_3 = models.TextField(blank=True, null=True)

    # Projects (Up to 3 entries)
    project_title_1 = models.CharField(max_length=255, blank=True, null=True)
    project_description_1 = models.TextField(blank=True, null=True)
    project_link_1 = models.URLField(blank=True, null=True)

    project_title_2 = models.CharField(max_length=255, blank=True, null=True)
    project_description_2 = models.TextField(blank=True, null=True)
    project_link_2 = models.URLField(blank=True, null=True)

    project_title_3 = models.CharField(max_length=255, blank=True, null=True)
    project_description_3 = models.TextField(blank=True, null=True)
    project_link_3 = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
