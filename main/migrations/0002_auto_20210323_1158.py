# Generated by Django 3.0.4 on 2021-03-23 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]