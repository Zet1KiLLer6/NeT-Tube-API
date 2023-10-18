from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from helper.models import CreatedUpdatedMixin
from helper.utils import generate_unique_slug
from django.contrib.auth import get_user_model
import datetime

User = get_user_model()


class Genre(models.Model):
    slug = models.SlugField(primary_key=True)
    name = models.CharField(max_length=20, unique=True)
    parent = models.ForeignKey('Genre', on_delete=models.CASCADE, related_name='childs', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(Genre, self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        if self.parent:
            return f'{self.parent} --> {self.name}'
        return f'{self.name}'


class Year(models.Model):
    year = models.SmallIntegerField(primary_key=True, validators=[
        MinValueValidator(1895),
        MaxValueValidator(2023)
    ])
    def __str__(self):
        return f'{self.year}'


class Country(models.Model):
    country = models.CharField(max_length=30, primary_key=True)

    def __str__(self):
        return f'{self.country}'


class Author(models.Model):
    author_name = models.CharField(max_length=50, primary_key=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='authors')

    def __str__(self):
        return f'{self.author}'


class PublicationName(CreatedUpdatedMixin):
    slug = models.SlugField(primary_key=True)
    title = models.CharField(unique=True, max_length=70)
    genre = models.ManyToManyField(Genre, related_name='publication_names')
    author = models.ManyToManyField(Author, related_name='publication_names')
    description = models.TextField()
    year = models.ManyToManyField(Year, related_name='publication_names')
    age_rating = models.SmallIntegerField(validators=[
        MinValueValidator(0),
        MaxValueValidator(18)
    ], blank=True, null=True)
    image = models.ImageField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(PublicationName, self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}'
