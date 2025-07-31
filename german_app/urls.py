from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LessonViewSet, LessonPropertyViewSet, RegisterUserView

router = DefaultRouter()
router.register(r'lessons', LessonViewSet)
router.register(r'properties', LessonPropertyViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterUserView.as_view(), name='register'),
]
