# Generated by Django 3.2.8 on 2022-08-17 20:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('threat', '0003_alter_threat_danger_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='threat',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Updated at'),
            preserve_default=False,
        ),
    ]
