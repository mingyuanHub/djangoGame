# Generated by Django 2.2.3 on 2019-07-04 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0006_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='desc',
            field=models.CharField(default='', max_length=250, verbose_name='座右铭'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default='', max_length=250, verbose_name='姓名'),
        ),
    ]
