# Generated by Django 2.2.2 on 2019-06-17 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0004_rental_landlord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintrequest',
            name='priority',
            field=models.CharField(default='low', max_length=20),
        ),
        migrations.AlterField(
            model_name='maintrequest',
            name='status',
            field=models.CharField(default='new', max_length=20),
        ),
    ]
