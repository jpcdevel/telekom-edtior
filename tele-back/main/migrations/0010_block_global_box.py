# Generated by Django 3.2.4 on 2021-08-21 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20210821_0637'),
    ]

    operations = [
        migrations.AddField(
            model_name='block',
            name='global_box',
            field=models.BooleanField(default=True),
        ),
    ]
