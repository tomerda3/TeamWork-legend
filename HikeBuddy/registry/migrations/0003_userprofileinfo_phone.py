# Generated by Django 3.2.9 on 2021-12-22 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0002_userprofileinfo_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='phone',
            field=models.CharField(default=None, max_length=10),
        ),
    ]
