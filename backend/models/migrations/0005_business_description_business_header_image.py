# Generated by Django 5.0.2 on 2024-03-04 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0004_alter_category_slug_alter_contentschedule_categories_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='description',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='business',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='businesses/'),
        ),
    ]