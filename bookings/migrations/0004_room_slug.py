# Generated by Django 3.2.19 on 2023-05-26 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0003_auto_20230524_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='slug',
            field=models.SlugField(max_length=200, null=True, unique=True),
        ),
    ]
