from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EtudiantViewSet, CoursViewSet, ProfesseurViewSet

router = DefaultRouter()
router.register(r'etudiants', EtudiantViewSet)
router.register(r'cours', CoursViewSet)
router.register(r'professeurs', ProfesseurViewSet)

urlpatterns = [
    path('', include(router.urls)),
]