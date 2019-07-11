# Generated by Django 2.1.7 on 2019-06-26 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20190626_1624'),
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('nid', models.BigAutoField(primary_key=True, serialize=False)),
                ('newsimages', models.ImageField(blank=True, max_length=1000, null=True, upload_to='static/images/', verbose_name='新闻动图')),
            ],
        ),
        migrations.AlterField(
            model_name='about',
            name='aboutimage',
            field=models.ImageField(blank=True, max_length=1000, null=True, upload_to='static/images/', verbose_name='关于动图'),
        ),
    ]
