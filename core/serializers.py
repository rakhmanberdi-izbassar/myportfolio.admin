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
    typingText = serializers.SerializerMethodField()
    imgUrl = serializers.SerializerMethodField()

    class Meta:
        model = Hero
        fields = [
            "name", "title", "subtitle", "description",
            "btn_text", "btn_url", "typingText", "imgUrl"
        ]

    def get_typingText(self, obj):
        return [
            obj.typing_text_1, obj.typing_delay_1,
            obj.typing_text_2, obj.typing_delay_2
        ]

    def get_imgUrl(self, obj):
        if obj.image:
            return obj.image.url
        return None


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'
