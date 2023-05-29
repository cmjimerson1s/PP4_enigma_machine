# Generated by Django 3.2.19 on 2023-05-25 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='tags',
            field=models.CharField(choices=[('Promotion', 'Promotion'), ('Sale', 'Sale'), ('News', 'News'), ('Partner Advert', 'Partner Advert'), ('Holiday', 'Holiday'), ('B.T.S', 'B.T.S'), ('Meet the Staff', 'Meet the Staff')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='posted_date',
            field=models.DateField(auto_now=True),
        ),
    ]