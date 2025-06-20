from django.urls import path
from .views import BrandListView, TestimonialView

urlpatterns = [
    path('brands/', BrandListView.as_view()),
    path('testimonials/', TestimonialView.as_view()),
]
