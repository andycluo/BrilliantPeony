# Generated by Django 2.1.7 on 2019-06-26 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20190626_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='newsimages',
            field=models.ImageField(blank=True, max_length=1000, null=True, upload_to='testdir/', verbose_name='新闻动图'),
        ),
    ]