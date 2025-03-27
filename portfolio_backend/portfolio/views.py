from rest_framework import viewsets
from django.core.mail import send_mail
from django.conf import settings
import logging
from .models import Project, Skill, Achievement, ContactMessage
from .serializers import ProjectSerializer, SkillSerializer, AchievementSerializer, ContactMessageSerializer

logger = logging.getLogger(__name__)  

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer

class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer

    def perform_create(self, serializer):
        contact_message = serializer.save()  

        recipient_email = contact_message.email  
        subject = contact_message.subject  
        message = contact_message.message  
        
        if not recipient_email: 
            logger.error("Email field is empty!")
            return
        
        sender_email = settings.EMAIL_HOST_USER

        try:
            send_mail(subject, message, sender_email, [recipient_email], fail_silently=False)
            logger.info(f"Email sent successfully to: {recipient_email}")
        except Exception as e:
            logger.error(f"Email failed to send: {e}")
