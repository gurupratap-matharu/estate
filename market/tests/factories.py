import factory
from market.models import Apartment, House


class HouseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = House

    square_footage = factory.Faker('random_element', elements=[x for x in range(100, 10000, 50)])
    num_bedrooms = factory.Faker('random_element', elements=[x for x in range(1, 11)])
    num_bathrooms = factory.Faker('random_element', elements=[x for x in range(1, 11)])
    num_stories = factory.Faker('random_element', elements=[x for x in range(1, 6)])
    garage = factory.Faker('random_element', elements=[x[0] for x in House.GARAGE_CHOICES])
    yard_fenced = factory.Faker('boolean')
    price = factory.Faker('random_element', elements=[x for x in range(150000, 10000000, 10000)])


class ApartmentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Apartment

    square_footage = factory.Faker('random_element', elements=[x for x in range(100, 10000, 50)])
    num_bedrooms = factory.Faker('random_element', elements=[x for x in range(1, 11)])
    num_bathrooms = factory.Faker('random_element', elements=[x for x in range(1, 11)])
    balcony = factory.Faker('boolean')
    laundry = factory.Faker('random_element', elements=[x[0] for x in Apartment.LAUNDRY_CHOICES])
    price = factory.Faker('random_element', elements=[x for x in range(150000, 10000000, 10000)])
