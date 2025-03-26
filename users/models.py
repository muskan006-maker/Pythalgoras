from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('superadmin', 'Superadmin'),
        ('admin', 'Admin'),
        ('instructor', 'Instructor'),
        ('trainee', 'Trainee'),
        ('guest', 'Guest'),
    ]
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='guest')
    
    def is_superadmin(self):
        return self.role == 'superadmin'

    def is_admin(self):
        return self.role == 'admin'

    def is_instructor(self):
        return self.role == 'instructor'

    def is_trainee(self):
        return self.role == 'trainee'
