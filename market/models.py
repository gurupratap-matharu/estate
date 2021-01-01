import uuid

from django.db import models
from django.urls import reverse


class Property(models.Model):
    """
    Abstract Property model which won't be registered in the database.
    Meant as a place holder to store common attributes among all properties
    """
    RENT = 'RT'
    SALE = 'SL'

    OFFER_CHOICES = [
        (RENT, 'Rent'),
        (SALE, 'Sale'),
    ]

    square_footage = models.PositiveIntegerField(verbose_name='Area in sqft')
    num_bedrooms = models.PositiveSmallIntegerField('Number of bedrooms')
    num_bathrooms = models.PositiveSmallIntegerField('Number of bathrooms')
    offer = models.CharField(choices=OFFER_CHOICES, default=SALE)
    price = models.DecimalField(max_digits=10, decimal_places=0)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-updated_on', ]


class House(Property):
    ATTACHED = 'AT'
    DETACHED = 'DT'
    NONE = 'NO'

    GARAGE_CHOICES = [
        (ATTACHED, 'Attached'),
        (DETACHED, 'Detached'),
        (NONE, 'None'),
    ]

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    num_stories = models.PositiveSmallIntegerField('Number of stories')
    garage = models.CharField(max_length=2, choices=GARAGE_CHOICES, default=ATTACHED)
    yard_fenced = models.BooleanField('Is the yard fenced?', default=True)

    def __str__(self):
        return f'{self.square_footage}sqft-{self.num_stories}stories-${self.price}'

    def get_absolute_url(self):
        return reverse('market:house_detail', args=[str(self.id)])


class Apartment(Property):
    ENSUITE = 'EN'
    COIN = 'CO'
    OFFSITE = 'OF'

    LAUNDRY_CHOICES = [
        (ENSUITE, 'Ensuite'),
        (COIN, 'Coin'),
        (OFFSITE, 'Offsite'),
    ]

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    balcony = models.BooleanField('Has a balcony?', default=True)
    laundry = models.CharField(max_length=2, choices=LAUNDRY_CHOICES, default=ENSUITE)

    def __str__(self):
        return f'{self.square_footage}sqft-${self.price}'

    def get_absolute_url(self):
        return reverse('market:apartment_detail', args=[str(self.id)])
