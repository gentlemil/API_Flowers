from django.db import models
from django.utils import timezone
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(
        max_length=100,
        blank= False, null=False, default='',
        unique=True,
        verbose_name='Name',
        help_text='',
    )

    slug = models.SlugField(
        max_length=100,
        blank= False, null=False, default='',
        unique=True,
        verbose_name='Slug name',
        help_text='',
        )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


# ----------------------------------------------------
class Room(models.Model):
    name = models.CharField(
        max_length=100,
        blank= False, null=False, default='',
        unique=True,
        verbose_name='Name',
        help_text='',
    )

    TEMPERATURE_CHOICE = [
    (1, 'cold'),
    (2, 'medium'),
    (3, 'warm'),
    ]

    temperature = models.IntegerField(
        choices=TEMPERATURE_CHOICE,
        verbose_name='Temperature',
        blank=False, null=False,
        help_text='',
    )

    EXPOSURE_CHOICE = (
    ('dark', 'dark'),
    ('shade', 'shade'),
    ('partysun', 'part sun'),
    ('fullsun', 'full sun'),
    )

    expose = models.CharField(
        max_length=10, choices=EXPOSURE_CHOICE,
        verbose_name="Amount of sun",
        blank=False, null=False,
        help_text='',
    )
    
    HUMIDITY_CHOICE = [
    (1, 'low'),
    (2, 'medium'),
    (3, 'high'),
    ]

    humidity = models.CharField(
        max_length=10, choices=HUMIDITY_CHOICE,
        verbose_name="Humidity",
        blank=False, null=False,
        help_text='',
    )
    draft = models.BooleanField(
        blank=True, null=False,
        default=False,
        verbose_name='',
    )

    def __str__(self):
        pass

    class Meta:
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'



# ----------------------------------------------------
class Plant(models.Model):
    name = models.CharField(
        max_length=100,
        blank= False, null=False, default='',
        unique=True,
        verbose_name='Name',
        help_text='',
    )

    category = models.ForeignKey(
        Category, on_delete=models.PROTECT,
        default=None, null=False, blank=False,
        verbose_name="Plant's category",
        help_text='',
    )
    room = models.ForeignKey(
        Room, on_delete=models.SET_NULL,
        default=None, null=True, blank=True,
        verbose_name="Plant's room",
        help_text='',
    )
    watering_interval = models.PositiveIntegerField(
        blank= False, null=False,
        verbose_name='Watering interval',
        help_text='In seconds',
    )
    fertilizing_interval = models.PositiveIntegerField(
        blank= False, null=False,
        verbose_name='Fertilizing interval',
        help_text='In seconds',
    )
    required_exposure = models.CharField(
        max_length=100,
        blank= False,
        null=False,
        default='',
        verbose_name='Name',
        help_text='',
        choices=Room.EXPOSURE_CHOICE,
    )

    required_temperature = models.CharField(
        max_length=100,
        default=False, blank= False, null=False,
        verbose_name='Name',
        help_text='',
    )

    required_humidity = models.CharField(
        max_length=100,
        default=False, blank= False, null=False,
        verbose_name='Name',
        help_text='',
    )
    blooming = models.BooleanField(
        default=False, blank=True, null=False,
        verbose_name='Blooming?',
        help_text='',
    )

    DIFICULTY_CHOICE = (
    (1, 'beginner'),
    (2, 'medium-low'),
    (2, 'medium'),
    (2, 'medium-high'),
    (2, 'high'),
    )

    difficulty = models.IntegerField(
        blank=False, null=False,
        verbose_name='',
        choices=DIFICULTY_CHOICE,
        help_text='',
        )
    
    last_watered = models.DateTimeField(
        default=None, null=True, blank=True,
        verbose_name='Last watering timestamp',
        help_text='',
    )

    last_fertilized = models.DateTimeField(
        default=None, null=True, blank=True,
        verbose_name='Last watering timestamp',
        help_text='',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Plant'
        verbose_name_plural = 'Plants'

