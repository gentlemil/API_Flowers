# Generated by Django 2.2.10 on 2020-02-15 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0004_auto_20200210_2055'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='plant',
            options={'verbose_name': 'Plant', 'verbose_name_plural': 'Plants'},
        ),
        migrations.AlterModelOptions(
            name='room',
            options={'verbose_name': 'Room', 'verbose_name_plural': 'Rooms'},
        ),
    ]
