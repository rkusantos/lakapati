# Generated by Django 4.1.2 on 2023-01-08 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('functions', '0003_farmdetails_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmdetails',
            name='farm_name',
            field=models.CharField(max_length=100),
        ),
    ]
