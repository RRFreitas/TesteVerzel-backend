# Generated by Django 3.2.13 on 2022-08-25 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classesmodules', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
