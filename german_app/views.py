from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from .models import Lesson, LessonProperty, User
from .serializers import LessonSerializer, LessonPropertySerializer, UserSerializer


class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [AllowAny]


class LessonPropertyViewSet(viewsets.ModelViewSet):
    queryset = LessonProperty.objects.all()
    serializer_class = LessonPropertySerializer
    permission_classes = [AllowAny]
