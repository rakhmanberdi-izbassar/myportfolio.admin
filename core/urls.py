from django.urls import path
from .views import ProjectListView, SkillListView, AboutDetailView, ContactMessageView, HeroDetailView, ExperienceListView
from .views import BrandListView, TestimonialView

urlpatterns = [
    path('projects/', ProjectListView.as_view()),
    path('skills/', SkillListView.as_view()),
    path('about/', AboutDetailView.as_view()),
    path('contact/', ContactMessageView.as_view()),
    path('brands/', BrandListView.as_view()),
    path('testimonials/', TestimonialView.as_view()),
    path('hero/', HeroDetailView.as_view()),
    path('experience/', ExperienceListView.as_view()),

]
