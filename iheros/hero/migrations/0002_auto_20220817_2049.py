# Generated by Django 3.2.8 on 2022-08-17 20:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='launch_time',
            field=models.DateTimeField(auto_now_add=True, default='2022-08-17 20:00:00', verbose_name='Launch time'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hero',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Updated at'),
            preserve_default=False,
        ),
    ]
