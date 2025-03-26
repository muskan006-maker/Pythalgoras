from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profession = models.CharField(max_length=100, blank=True)
    headline = models.CharField(max_length=100,blank=True,null=True)
    slogan = models.CharField(max_length=100,blank=True,null=True)
    location_city = models.CharField(max_length=100,blank=True,null=True)
    location_state = models.CharField(max_length=100,blank=True,null=True)
    location_country = models.CharField(max_length=100,blank=True,null=True)



    def __str__(self):
        return f'{self.user.username} Profile'


class Projects(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    projects_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    institution = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

class Skill(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)