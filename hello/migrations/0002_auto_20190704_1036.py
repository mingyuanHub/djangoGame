# Generated by Django 2.2.3 on 2019-07-04 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='test2',
            name='age1',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='test2',
            name='age3',
            field=models.IntegerField(default=2),
        ),
    ]
