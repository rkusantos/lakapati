# Generated by Django 4.1.2 on 2023-01-08 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('functions', '0002_farmdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmdetails',
            name='desc',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
