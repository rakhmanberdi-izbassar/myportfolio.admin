# core/models.py

from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    link = models.URLField(blank=True)
    technologies = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=50)  # beginner/intermediate/expert

    def __str__(self):
        return self.name

class About(models.Model):
    bio = models.TextField()
    email = models.EmailField()
    telegram = models.URLField(blank=True)
