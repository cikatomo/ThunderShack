# Generated by Django 3.0.6 on 2020-07-21 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('private_messages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='privatemessage',
            name='title',
        ),
    ]
