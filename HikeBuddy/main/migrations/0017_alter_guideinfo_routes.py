# Generated by Django 3.2.9 on 2021-12-30 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20211229_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guideinfo',
            name='routes',
            field=models.CharField(default='None', max_length=1000),
        ),
    ]
