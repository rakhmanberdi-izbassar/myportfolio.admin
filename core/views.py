from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project, Skill, About, ContactMessage
from .serializers import ProjectSerializer, SkillSerializer, AboutSerializer, ContactMessageSerializer

from portfolio.models import Brand, Testimonial, TestimonialSection
from portfolio.serializers import BrandSerializer, TestimonialSerializer, TestimonialSectionSerializer
from .models import Hero
from .serializers import HeroSerializer, ExperienceSerializer
from .models import SocialLink
from .serializers import SocialLinkSerializer


class ProjectListView(APIView):
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

class SkillListView(APIView):
    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data)

class AboutDetailView(APIView):
    def get(self, request):
        about = About.objects.first()
        serializer = AboutSerializer(about)
        return Response(serializer.data)

class BrandListView(APIView):
    def get(self, request):
        brands = Brand.objects.all()
        serializer = BrandSerializer(brands, many=True)
        return Response(serializer.data)

class TestimonialView(APIView):
    def get(self, request):
        testimonials = Testimonial.objects.all()
        section = TestimonialSection.objects.first()
        data = {
            "sectionHeading": TestimonialSectionSerializer(section).data if section else {},
            "allTestimonial": TestimonialSerializer(testimonials, many=True).data
        }
        return Response(data)

class ContactMessageView(APIView):
    def post(self, request):
        serializer = ContactMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Хабарлама жіберілді!'}, status=201)
        return Response(serializer.errors, status=400)

class HeroDetailView(APIView):
    def get(self, request):
        hero = Hero.objects.first()
        serializer = HeroSerializer(hero)
        return Response(serializer.data)
    
from .models import Experience
from .serializers import ExperienceSerializer

class ExperienceListView(APIView):
    def get(self, request):
        experiences = Experience.objects.order_by('-start_date')
        serializer = ExperienceSerializer(experiences, many=True)
        return Response(serializer.data)

class SocialLinkListView(APIView):
    def get(self, request):
        links = SocialLink.objects.all()
        serializer = SocialLinkSerializer(links, many=True)
        return Response(serializer.data)