from rest_framework import serializers
from .models import User, Lesson, LessonProperty


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LessonPropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonProperty
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    property = LessonPropertySerializer(read_only=True)
    property_id = serializers.PrimaryKeyRelatedField(
        queryset=LessonProperty.objects.all(), source='property', write_only=True)

    class Meta:
        model = Lesson
        fields = ['id', 'title', 'property', 'property_id']
