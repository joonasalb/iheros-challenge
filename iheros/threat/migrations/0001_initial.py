# Generated by Django 3.2.8 on 2022-08-16 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Threat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monster_name', models.CharField(max_length=100, verbose_name='Monster name')),
                ('danger_level', models.CharField(choices=[('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C')], default='S', max_length=20, verbose_name='Rank')),
                ('location', models.CharField(max_length=100, verbose_name='location')),
                ('defeated_by', models.CharField(max_length=100, verbose_name='defeated_by')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
            ],
            options={
                'verbose_name': 'Threat',
                'verbose_name_plural': 'Threats',
            },
        ),
    ]