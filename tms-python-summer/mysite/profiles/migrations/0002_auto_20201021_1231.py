# Generated by Django 3.1.2 on 2020-10-21 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='info',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='add info'),
        ),
    ]
