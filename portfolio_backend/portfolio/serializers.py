from rest_framework import serializers
from .models import Project, Skill, Achievement, ContactMessage

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = '__all__'

class ContactMessageSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()  
    subject = serializers.CharField()  
    message = serializers.CharField()  

    class Meta:
        model = ContactMessage
        fields = ['email', 'subject', 'message', 'created_at']
