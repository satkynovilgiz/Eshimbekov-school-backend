from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)  # ← Убедись, что это есть
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='teacher_photos/', blank=True, null=True)

    def __str__(self):
        return self.name


