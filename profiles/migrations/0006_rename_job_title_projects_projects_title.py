# Generated by Django 5.1.6 on 2025-03-24 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_rename_experience_projects'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='job_title',
            new_name='projects_title',
        ),
    ]
