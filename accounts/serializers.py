from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model

# [AMS]:- User Serializer for API representation
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            'id', 'username', 'email', 'full_name',
            'phone_number', 'profile_picture'
            # 'is_quran_teacher', 'is_student' [AMS] for future role-based access control
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'profile_picture': {'required': False}
        }
    
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            full_name=validated_data.get('full_name', ''),
            phone_number=validated_data.get('phone_number', ''),
            # is_quran_teacher=validated_data.get('is_quran_teacher', False),
            # is_student=validated_data.get('is_student', True)
        )
        return user