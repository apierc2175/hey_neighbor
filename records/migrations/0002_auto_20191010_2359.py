# Generated by Django 2.2.6 on 2019-10-10 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='records',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='records',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
