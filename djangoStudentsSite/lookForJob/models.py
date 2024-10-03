from django.urls import reverse
from django.utils import timezone
from django.db import models
from django.utils.text import slugify


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=True)


class Job(models.Model):
    title = models.TextField(max_length=255)
    company = models.TextField(max_length=500)
    on_or_off = models.TextField(max_length=2)
    city = models.TextField(max_length=255, blank=True)
    full_or_part = models.TextField(max_length=10)
    salary = models.IntegerField()
    description = models.TextField(max_length=1000, blank=True)

    created_time = models.DateTimeField(auto_now_add=True)
    changed_time = models.DateTimeField(auto_now=True)

    # slug поле
    slug = models.SlugField(max_length=255, unique=True, editable=False)

    is_published = models.BooleanField(default=True)

    published = PublishedManager()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.slug = slugify(f"{self.pk}_{self.company}_{self.title}")
        super().save(update_fields=['slug'])

    def get_absolute_url(self):
        return reverse('job_blank', kwargs={'job_slug': self.slug})

    def __str__(self):
        return f"{self.pk} {self.company} {self.title}"
