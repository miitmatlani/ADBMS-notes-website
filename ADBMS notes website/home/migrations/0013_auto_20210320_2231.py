# Generated by Django 3.1.5 on 2021-03-20 17:01

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20210320_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='ph_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=10, region=None, unique=True),
        ),
    ]
