from django.contrib import admin
from .models import Project, Skill, Achievement, ContactMessage

admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Achievement)
admin.site.register(ContactMessage)
