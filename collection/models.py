from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


class Cast(models.Model):
    name = models.TextField()


class Movie(models.Model):
    title = models.TextField()
    summary = models.TextField()
    ratings = models.ManyToManyField(User)
    cast = models.ManyToManyField(Cast)


class Song(models.Model):
    title = models.TextField()
    content = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)


class Lyric(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.TextField()
    favorites = models.ManyToManyField(User)
