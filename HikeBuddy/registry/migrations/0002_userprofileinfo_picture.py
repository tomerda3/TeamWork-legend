# Generated by Django 3.2.9 on 2021-12-19 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='picture',
            field=models.ImageField(blank=True, upload_to='profile_pics'),
        ),
    ]
