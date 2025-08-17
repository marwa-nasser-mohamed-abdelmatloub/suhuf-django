from django.db import models

class Program(models.Model):
    name = models.CharField(max_length=255, verbose_name="اسم البرنامج")
    description = models.TextField(verbose_name="وصف البرنامج", blank=True, null=True)
    image = models.ImageField(upload_to='program_images/', blank=True, null=True, verbose_name="صورة البرنامج")
    is_active = models.BooleanField(default=True, verbose_name="نشط")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاريخ التحديث")

    class Meta:
        verbose_name = "برنامج"
        verbose_name_plural = "البرامج"
        ordering = ['-created_at']

    def __str__(self):
        return self.name
