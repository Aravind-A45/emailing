# Generated by Django 4.2.3 on 2023-11-18 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invention', '0006_alter_category_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
