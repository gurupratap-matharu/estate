# Generated by Django 3.1.4 on 2021-01-01 18:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('square_footage', models.PositiveIntegerField(verbose_name='Area in sqft')),
                ('num_bedrooms', models.PositiveSmallIntegerField(verbose_name='Number of bedrooms')),
                ('num_bathrooms', models.PositiveSmallIntegerField(verbose_name='Number of bathrooms')),
                ('offer', models.CharField(choices=[('RT', 'Rent'), ('SL', 'Sale')], default='SL', max_length=2)),
                ('price', models.DecimalField(decimal_places=0, max_digits=10)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('balcony', models.BooleanField(default=True, verbose_name='Has a balcony?')),
                ('laundry', models.CharField(choices=[('EN', 'Ensuite'), ('CO', 'Coin'), ('OF', 'Offsite')], default='EN', max_length=2)),
            ],
            options={
                'ordering': ['-updated_on'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('square_footage', models.PositiveIntegerField(verbose_name='Area in sqft')),
                ('num_bedrooms', models.PositiveSmallIntegerField(verbose_name='Number of bedrooms')),
                ('num_bathrooms', models.PositiveSmallIntegerField(verbose_name='Number of bathrooms')),
                ('offer', models.CharField(choices=[('RT', 'Rent'), ('SL', 'Sale')], default='SL', max_length=2)),
                ('price', models.DecimalField(decimal_places=0, max_digits=10)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('num_stories', models.PositiveSmallIntegerField(verbose_name='Number of stories')),
                ('garage', models.CharField(choices=[('AT', 'Attached'), ('DT', 'Detached'), ('NO', 'None')], default='AT', max_length=2)),
                ('yard_fenced', models.BooleanField(default=True, verbose_name='Is the yard fenced?')),
            ],
            options={
                'ordering': ['-updated_on'],
                'abstract': False,
            },
        ),
    ]
