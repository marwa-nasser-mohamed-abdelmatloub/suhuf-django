from django.db import models

# Create your models here.

class Course(models.Model):
    LEVEL_CHOICES = [
        ('beginner', 'مبتدئ'),
        ('intermediate', 'متوسط'),
        ('advanced', 'متقدم'),
    ]
    
    title = models.CharField(max_length=255, verbose_name="عنوان الكورس")
    description = models.TextField(verbose_name="وصف الكورس")
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True, verbose_name="السعر")
    image = models.ImageField(upload_to='course_images/', blank=True, null=True, verbose_name="صورة الكورس")
    duration = models.CharField(max_length=100, blank=True, null=True, verbose_name="مدة الكورس")
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='beginner', verbose_name="مستوى الكورس")
    instructor = models.CharField(max_length=255, blank=True, null=True, verbose_name="المدرب")
    is_active = models.BooleanField(default=True, verbose_name="نشط")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاريخ التحديث")

    class Meta:
        verbose_name = "كورس"
        verbose_name_plural = "الكورسات"
        ordering = ['-created_at']

    def __str__(self):
        return self.title