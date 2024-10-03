from django.urls import reverse
from django.utils import timezone
from django.db import models
from django.utils.text import slugify

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Student.Status.PUBLISHED)

class Student(models.Model):
    # класс для определения перечислений (для чисел)
    class Status(models.IntegerChoices):
        DRAFT = (0, 'draft blank')
        PUBLISHED = (1, 'published')

    gender = models.TextField(max_length=1)
    name = models.TextField(max_length=255)
    surname = models.TextField(max_length=255)
    age = models.IntegerField()
    phone = models.TextField(max_length=255, unique=True)
    email = models.TextField(max_length=255, unique=True)
    university = models.TextField(max_length=255)
    specialization = models.TextField(max_length=255)
    # внешний ключ Many to Many
    # имя в поле после миграции будет имя_id, но мы в shell например, все равно сможем обращаться к:
    # category - будет возвращаться объект другой таблицы, с которым тоже можно работать
    # category_id - будет возвращаться ид категории
    category = models.ForeignKey('SpecializationCategory', on_delete=models.CASCADE, related_name='category')
    degree = models.TextField(max_length=255)
    course = models.IntegerField()
    description = models.TextField(max_length=1000, blank=True)

    created_time = models.DateTimeField(auto_now_add=True)
    changed_time = models.DateTimeField(auto_now=True)

    # slug поле
    slug = models.SlugField(max_length=255, unique=True, editable=False)

    # передаем вторым параметром класс, которой определяет,
    # что будет отображаться в, например, админке по полю is_published
    is_published = models.BooleanField(default=Status.PUBLISHED, choices=Status.choices)

    objects = models.Manager()
    published = PublishedManager()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.slug = slugify(f"{self.pk}_{self.name}_{self.surname}_{self.specialization}")
        super().save(update_fields=['slug'])

    def get_absolute_url(self):
        return reverse('student_blank', kwargs={'student_slug': self.slug})

    def __str__(self):
        return f"{self.pk} {self.name} {self.surname} {self.age}"


class SpecializationCategory(models.Model):
    name = models.TextField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, editable=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.slug = slugify(f"{self.pk}_{self.name}")
        super().save(update_fields=['slug'])

    def get_absolute_url(self):
        return reverse('specialization_category', kwargs={'category_slug': self.slug})