from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('student', 'Student'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class LessonProperty(models.Model):
    type = models.CharField(max_length=100)
    subtype = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.type} - {self.subtype}"


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    property = models.ForeignKey(LessonProperty, on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
