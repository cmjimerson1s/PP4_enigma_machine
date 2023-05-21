# Generated by Django 3.2.19 on 2023-05-21 19:28

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('blog_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('blog_blurb', models.TextField(blank=True)),
                ('blog_content', models.TextField()),
                ('posted_date', models.DateTimeField(auto_now=True)),
                ('meta_tags', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'ordering': ['-posted_date'],
            },
        ),
    ]
