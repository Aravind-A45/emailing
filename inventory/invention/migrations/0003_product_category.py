# Generated by Django 4.2.3 on 2023-11-18 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invention', '0002_alter_logs_options_cart_product_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='invention.category'),
            preserve_default=False,
        ),
    ]
