# Generated by Django 3.2.4 on 2021-08-20 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210820_2205'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='block',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='row',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='block',
            name='btn_view',
            field=models.CharField(default='primary', max_length=10),
        ),
    ]
