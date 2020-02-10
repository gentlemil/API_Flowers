# Generated by Django 3.0.2 on 2020-02-08 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, unique=True, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, unique=True, verbose_name='Name')),
                ('temperature', models.IntegerField(choices=[('cold', 'cold'), ('medium', 'medium'), ('warm', 'warm')], max_length=10, verbose_name='Temperature')),
                ('expose', models.CharField(choices=[('dark', 'dark'), ('shade', 'shade'), ('partysun', 'part sun'), ('fullsun', 'full sun')], max_length=10, verbose_name='Amount of sun')),
                ('humidity', models.CharField(choices=[(1, 'low'), (2, 'medium'), (3, 'high')], max_length=10, verbose_name='Humidity')),
                ('draft', models.BooleanField(blank=True, verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, unique=True, verbose_name='Name')),
                ('watering_interval', models.PositiveIntegerField(help_text='In days', verbose_name='Watering interval')),
                ('fertilizing_interval', models.PositiveIntegerField(help_text='In days', verbose_name='Fertilizing interval')),
                ('required_exposure', models.CharField(choices=[('dark', 'dark'), ('shade', 'shade'), ('partysun', 'part sun'), ('fullsun', 'full sun')], default='', max_length=100, verbose_name='Name')),
                ('required_humidity', models.CharField(default=False, max_length=100, verbose_name='Name')),
                ('blooming', models.BooleanField(blank=True, default=False, verbose_name='Blooming?')),
                ('difficulty', models.IntegerField(choices=[(1, 'beginner'), (2, 'medium-low'), (2, 'medium'), (2, 'medium-high'), (2, 'high')], verbose_name='')),
                ('last_watered', models.DateField(blank=True, default=None, null=True, verbose_name='')),
                ('last_fertilized', models.DateField(blank=True, default=None, null=True, verbose_name='')),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='plants.Category', verbose_name="Plant's category")),
                ('room', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='plants.Room', verbose_name="Plant's room")),
            ],
        ),
    ]
