from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Band(models.Model):

    def __str__(self):
        return f'{self.name}' #Nom du groupe
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(default='AR', choices=Genre.choices, max_length=10)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(default=2000,
    validators=[MinValueValidator(1900), MaxValueValidator(2021)]
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)

class Listing(models.Model):
    name = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=500)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(validators=[MaxValueValidator(2024), MinValueValidator(1900)])
    class Type(models.TextChoices):
        RECORDS = "disques"
        CLOTHING = "vetements"
        POSTERS = "affiches"
        MISCELLANEOUS = "divers"
    type = models.fields.CharField(choices=Type.choices, max_length=10)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)