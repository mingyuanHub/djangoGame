# Generated by Django 2.2.3 on 2019-07-04 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_auto_20190704_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='test2',
            name='age4',
            field=models.IntegerField(default=2, max_length=3),
        ),
    ]