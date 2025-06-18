from rest_framework import serializers
from .models import Brand, Testimonial, TestimonialSection

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
