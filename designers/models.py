from django.db import models
from django.urls import reverse


class Designer(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    email = models.EmailField(blank=True)
    country = models.CharField(max_length=128)
    collection = models.CharField(max_length=128)
    biographie = models.TextField(blank=True)
    thumbnail = models.ImageField(
        upload_to='designers', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('designer', kwargs={'slug': self.slug})
