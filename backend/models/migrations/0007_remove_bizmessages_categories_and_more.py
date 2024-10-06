# Generated by Django 4.2 on 2024-10-01 19:11

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0006_business_display_name_business_favicon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bizmessages',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='bizmessages',
            name='is_sent',
        ),
        migrations.RemoveField(
            model_name='bizmessages',
            name='send_at',
        ),
        migrations.CreateModel(
            name='MessageCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('send_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='send at')),
                ('is_sent', models.BooleanField(default=False, verbose_name='is sent')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='models.category', verbose_name='קטגוריה')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='models.bizmessages', verbose_name='הודעה')),
            ],
            options={
                'verbose_name': 'message category',
                'verbose_name_plural': 'message categories',
            },
        ),
    ]
