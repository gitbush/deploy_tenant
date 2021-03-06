# Generated by Django 2.2.2 on 2019-06-17 12:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('maintenance', '0003_auto_20190617_1337'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rental', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='maintenance.Rental')),
                ('requests', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='maintenance.MaintRequest')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
