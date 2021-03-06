# Generated by Django 3.1.2 on 2020-10-15 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_auto_20201012_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='category_article', to='blog.category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.CharField(max_length=300),
        ),
    ]
