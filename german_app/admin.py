from django.contrib import admin
from .models import User, Lesson, LessonProperty

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'is_staff')

@admin.register(LessonProperty)
class LessonPropertyAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'subtype')

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'property')

