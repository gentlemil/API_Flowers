# Generated by Django 2.2.10 on 2020-02-15 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0007_auto_20200215_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=100, unique=True, verbose_name='Slug name'),
        ),
    ]
