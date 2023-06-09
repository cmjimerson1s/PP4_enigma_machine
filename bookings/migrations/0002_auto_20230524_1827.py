# Generated by Django 3.2.19 on 2023-05-24 18:27

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='blog_image',
            new_name='detail_image',
        ),
        migrations.AddField(
            model_name='room',
            name='short_room_description',
            field=models.CharField(max_length=250, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='room',
            name='small_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
