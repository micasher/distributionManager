# Generated by Django 4.2 on 2024-09-30 08:59

import core.utils
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0002_alter_business_options_alter_businessqr_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='business',
            options={'verbose_name': 'עסק', 'verbose_name_plural': 'עסקים'},
        ),
        migrations.AlterModelOptions(
            name='businessqr',
            options={'verbose_name': 'QR של עסק', 'verbose_name_plural': 'QR של עסקים'},
        ),
        migrations.AlterModelOptions(
            name='businessqrcategories',
            options={'verbose_name': 'קטגוריית QR של עסק', 'verbose_name_plural': 'קטגוריות QR של עסקים'},
        ),
        migrations.AlterModelOptions(
            name='categoriesclicks',
            options={'verbose_name': 'לחיצות קטגוריות', 'verbose_name_plural': 'לחיצות קטגוריות'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'קטגוריה', 'verbose_name_plural': 'קטגוריות'},
        ),
        migrations.AlterModelOptions(
            name='contentschedule',
            options={'ordering': ['-send_date', '-created_at'], 'verbose_name': 'לוח זמנים לתוכן', 'verbose_name_plural': 'לוחות זמנים לתוכן'},
        ),
        migrations.AlterModelOptions(
            name='leadsclicks',
            options={'verbose_name': 'לחיצות לידים', 'verbose_name_plural': 'לחיצות לידים'},
        ),
        migrations.AlterModelOptions(
            name='telegramgroup',
            options={'verbose_name': 'קבוצת טלגרם', 'verbose_name_plural': 'קבוצות טלגרם'},
        ),
        migrations.AlterModelOptions(
            name='whatsappgroup',
            options={'verbose_name': 'קבוצת וואטסאפ', 'verbose_name_plural': 'קבוצות וואטסאפ'},
        ),
        migrations.AlterField(
            model_name='business',
            name='description',
            field=models.TextField(blank=True, max_length=20000, null=True, verbose_name='תיאור'),
        ),
        migrations.AlterField(
            model_name='business',
            name='footer_image',
            field=models.ImageField(blank=True, null=True, upload_to='businesses/', verbose_name='תמונת תחתית'),
        ),
        migrations.AlterField(
            model_name='business',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='businesses/', verbose_name='תמונת כותרת'),
        ),
        migrations.AlterField(
            model_name='business',
            name='slug',
            field=models.SlugField(allow_unicode=True, max_length=100, unique=True, verbose_name='סלאג'),
        ),
        migrations.AlterField(
            model_name='businessqr',
            name='business',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qrs', to='models.business', verbose_name='עסק'),
        ),
        migrations.AlterField(
            model_name='businessqr',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qrs', to='models.businessqrcategories', verbose_name='קטגוריה'),
        ),
        migrations.AlterField(
            model_name='businessqr',
            name='qr_code',
            field=models.CharField(default=core.utils.generate_small_uuid, editable=False, max_length=100, unique=True, verbose_name='קוד QR'),
        ),
        migrations.AlterField(
            model_name='businessqr',
            name='qr_img',
            field=models.ImageField(blank=True, null=True, upload_to='qrs/', verbose_name='תמונת QR'),
        ),
        migrations.AlterField(
            model_name='categoriesclicks',
            name='business',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories_clicks', to='models.business', verbose_name='עסק'),
        ),
        migrations.AlterField(
            model_name='categoriesclicks',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories_clicks', to='models.category', verbose_name='קטגוריה'),
        ),
        migrations.AlterField(
            model_name='categoriesclicks',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='נוצר ב'),
        ),
        migrations.AlterField(
            model_name='categoriesclicks',
            name='group_type',
            field=models.CharField(choices=[('whatsapp', 'whatsapp'), ('telegram', 'telegram')], default='whatsapp', max_length=100, verbose_name='סוג קבוצה'),
        ),
        migrations.AlterField(
            model_name='categoriesclicks',
            name='qr',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories_clicks', to='models.businessqr', verbose_name='קוד QR'),
        ),
        migrations.AlterField(
            model_name='category',
            name='all_telegram_urls',
            field=models.ManyToManyField(related_name='telegram_categories', to='models.telegramgroup', verbose_name='כל קישורי טלגרם'),
        ),
        migrations.AlterField(
            model_name='category',
            name='all_whatsapp_urls',
            field=models.ManyToManyField(related_name='whatsapp_categories', to='models.whatsappgroup', verbose_name='כל קישורי וואטסאפ'),
        ),
        migrations.AlterField(
            model_name='category',
            name='business',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='models.business', verbose_name='עסק'),
        ),
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='categories/', verbose_name='אייקון'),
        ),
        migrations.AlterField(
            model_name='category',
            name='open_telegram_url',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='open_telegram_categories', to='models.telegramgroup', verbose_name='פתח קישור טלגרם'),
        ),
        migrations.AlterField(
            model_name='category',
            name='open_whatsapp_url',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='open_whatsapp_categories', to='models.whatsappgroup', verbose_name='פתח קישור וואטסאפ'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(allow_unicode=True, max_length=100, verbose_name='סלאג'),
        ),
        migrations.AlterField(
            model_name='contentschedule',
            name='approve_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='תאריך אישור'),
        ),
        migrations.AlterField(
            model_name='contentschedule',
            name='approve_state',
            field=models.CharField(choices=[('A', 'מאושר'), ('P', 'ממתין'), ('R', 'נדחה')], default='P', max_length=1, verbose_name='מצב אישור'),
        ),
        migrations.AlterField(
            model_name='contentschedule',
            name='business',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contentSchedules', to='models.business', verbose_name='עסק'),
        ),
        migrations.AlterField(
            model_name='contentschedule',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='contentSchedules', to='models.category', verbose_name='קטגוריות'),
        ),
        migrations.AlterField(
            model_name='contentschedule',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='נוצר ב'),
        ),
        migrations.AlterField(
            model_name='contentschedule',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='מזהה'),
        ),
        migrations.AlterField(
            model_name='contentschedule',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='contents/', verbose_name='תמונה'),
        ),
        migrations.AlterField(
            model_name='contentschedule',
            name='is_telegram_sent',
            field=models.BooleanField(default=False, verbose_name='האם נשלח בטלגרם'),
        ),
        migrations.AlterField(
            model_name='contentschedule',
            name='is_whatsapp_sent',
            field=models.BooleanField(default=False, verbose_name='האם נשלח בוואטסאפ'),
        ),
        migrations.AlterField(
            model_name='contentschedule',
            name='message',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='הודעה'),
        ),
        migrations.AlterField(
            model_name='contentschedule',
            name='send_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='תאריך שליחה'),
        ),
        migrations.AlterField(
            model_name='contentschedule',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='עודכן ב'),
        ),
        migrations.AlterField(
            model_name='leadsclicks',
            name='business',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leads_clicks', to='models.business', verbose_name='עסק'),
        ),
        migrations.AlterField(
            model_name='leadsclicks',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='נוצר ב'),
        ),
        migrations.AlterField(
            model_name='leadsclicks',
            name='qr',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='leads_clicks', to='models.businessqr', verbose_name='קוד QR'),
        ),
        migrations.AlterField(
            model_name='sysuser',
            name='business',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='models.business', verbose_name='עסק'),
        ),
        migrations.AlterField(
            model_name='telegramgroup',
            name='chat_id',
            field=models.CharField(max_length=120, verbose_name="מזהה צ'אט"),
        ),
        migrations.AlterField(
            model_name='telegramgroup',
            name='last_members_check',
            field=models.DateTimeField(blank=True, null=True, verbose_name='בדיקת חברים אחרונה'),
        ),
        migrations.AlterField(
            model_name='telegramgroup',
            name='last_members_count',
            field=models.PositiveIntegerField(default=0, verbose_name='מספר חברים אחרון'),
        ),
        migrations.AlterField(
            model_name='whatsappgroup',
            name='chat_id',
            field=models.CharField(max_length=120, verbose_name="מזהה צ'אט"),
        ),
        migrations.AlterField(
            model_name='whatsappgroup',
            name='last_members_check',
            field=models.DateTimeField(blank=True, null=True, verbose_name='בדיקת חברים אחרונה'),
        ),
        migrations.AlterField(
            model_name='whatsappgroup',
            name='last_members_count',
            field=models.PositiveIntegerField(default=0, verbose_name='מספר חברים אחרון'),
        ),
    ]