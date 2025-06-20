# core/serializers.py

from rest_framework import serializers
from .models import Project, Skill, About
from portfolio.models import Brand, Testimonial, TestimonialSection
from .models import ContactMessage
from .models import Hero
from .models import Experience


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['src', 'alt']

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ['avatar_img', 'review_text', 'avatar_name', 'avatar_company']

class TestimonialSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestimonialSection
        fields = ['mini_title', 'title']

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = '__all__'

class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = '__all__'

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'
