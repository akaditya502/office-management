# Generated by Django 3.2.6 on 2022-02-08 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.IntegerField(max_length=100),
        ),
    ]