from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            'id', 'title', 'description', 'price', 'image', 
            'duration', 'level', 'instructor', 'is_active', 
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
        extra_kwargs = {
            'level': {'required': False, 'allow_null': True},
            'price': {'required': False, 'allow_null': True},
            'title': {'required': True},
            'description': {'required': True},
            'instructor': {'required': True}
        }
    
    def validate_price(self, value):
        if value is not None and value <= 0:
            raise serializers.ValidationError("السعر يجب أن يكون أكبر من صفر")
        return value
    
    def validate_title(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError("عنوان الكورس يجب أن يكون 3 أحرف على الأقل")
        return value.strip()
    
    def validate_description(self, value):
        if len(value.strip()) < 10:
            raise serializers.ValidationError("الوصف يجب أن يكون 10 أحرف على الأقل")
        return value.strip()
    
    def validate_instructor(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError("اسم المعلم يجب أن يكون 3 أحرف على الأقل")
        return value.strip()