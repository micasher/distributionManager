# Generated by Django 4.2 on 2024-03-09 00:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0013_rename_is_sent_contentschedule_is_telegram_sent_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentschedule',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
