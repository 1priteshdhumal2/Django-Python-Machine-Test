# Generated by Django 5.1 on 2024-08-29 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_project_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='temp_field',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
