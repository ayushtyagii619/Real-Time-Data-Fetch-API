# Generated by Django 5.0.6 on 2024-08-27 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sabpaisa_app', '0002_newuser_groups_newuser_is_superuser_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
