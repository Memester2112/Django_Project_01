# Generated by Django 3.2.13 on 2022-05-26 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20220526_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
