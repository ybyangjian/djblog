# Generated by Django 2.0.4 on 2018-04-13 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoBlog', '0004_auto_20180413_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='readed_num',
            field=models.IntegerField(default=0),
        ),
    ]
