# Generated by Django 4.2.3 on 2023-11-18 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invention', '0004_logs_created_by_logs_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logs',
            name='created_by',
        ),
    ]
