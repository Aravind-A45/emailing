# Generated by Django 4.2.3 on 2023-11-18 12:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('invention', '0003_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='logs',
            name='created_by',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logs',
            name='status',
            field=models.CharField(choices=[('checked_in', 'checked_in'), ('checked_out', 'checked_out')], default=1, max_length=20),
            preserve_default=False,
        ),
    ]
