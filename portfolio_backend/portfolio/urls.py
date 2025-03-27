from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, SkillViewSet, AchievementViewSet, ContactMessageViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'achievements', AchievementViewSet)
router.register(r'contact-messages', ContactMessageViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
