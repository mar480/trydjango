# Generated by Django 2.0.7 on 2019-01-07 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20190107_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='featured',
            field=models.TextField(blank=True),
        ),
    ]
