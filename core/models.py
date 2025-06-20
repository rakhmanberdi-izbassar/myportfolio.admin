# core/models.py

from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    link = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
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
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    youtube = models.URLField(blank=True)
    profile_image = models.ImageField(upload_to='about/', blank=True, null=True)  # 👈 Жаңа өріс

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Hero(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    image = models.ImageField(upload_to='hero/')


class Experience(models.Model):
    position = models.CharField(max_length=255)        # Мысалы: Full Stack Developer
    company = models.CharField(max_length=255)         # Мысалы: Bilim App
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True) # null — қазіргі уақытқа дейін болса
    description = models.TextField()

    def __str__(self):
        return f"{self.position} at {self.company}"
