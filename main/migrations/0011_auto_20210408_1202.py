# Generated by Django 3.0.4 on 2021-04-08 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20210408_0704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='salary_max',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='salary_min',
            field=models.PositiveIntegerField(),
        ),
    ]
