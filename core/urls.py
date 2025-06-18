from django.urls import path
from .views import ProjectList, SkillList, AboutDetail

urlpatterns = [
    path('projects/', ProjectList.as_view(), name='projects'),
    path('skills/', SkillList.as_view(), name='skills'),
    path('about/', AboutDetail.as_view(), name='about'),
]
