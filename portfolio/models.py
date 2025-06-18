from django.db import models

class Brand(models.Model):
    src = models.URLField()
    alt = models.CharField(max_length=255)

class TestimonialSection(models.Model):
    mini_title = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

class Testimonial(models.Model):
    avatar_img = models.URLField()
    review_text = models.TextField()
    avatar_name = models.CharField(max_length=100)
    avatar_company = models.CharField(max_length=100)
