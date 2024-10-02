from django.utils import timezone
from django.db import models
from django.utils.text import slugify

class Student(models.Model):
    gender = models.TextField(max_length=1)
    name = models.TextField(max_length=255)
    surname = models.TextField(max_length=255)
    age = models.IntegerField()
    phone = models.TextField(max_length=255, unique=True)
    email = models.TextField(max_length=255, unique=True)
    university = models.TextField(max_length=255)
    specialization = models.TextField(max_length=255)
    degree = models.TextField(max_length=255)
    course = models.IntegerField()
    description = models.TextField(max_length=1000, blank=True)

    created_time = models.DateTimeField(auto_now_add=True)
    changed_time = models.DateTimeField(auto_now=True)

    # slug поле
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    is_published = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.pk}_{self.name}_{self.surname}_{self.specialization}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.pk} {self.name} {self.surname} {self.age}"
