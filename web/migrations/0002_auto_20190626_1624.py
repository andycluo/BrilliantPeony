# Generated by Django 2.1.7 on 2019-06-26 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='home',
            old_name='aid',
            new_name='hid',
        ),
    ]
