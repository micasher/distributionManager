# Generated by Django 5.0.2 on 2024-02-29 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='slug',
            field=models.SlugField(allow_unicode=True, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(allow_unicode=True, max_length=100, unique=True),
        ),
    ]
