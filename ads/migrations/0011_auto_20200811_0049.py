# Generated by Django 3.0.6 on 2020-08-11 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0010_ad_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]