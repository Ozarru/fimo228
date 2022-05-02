from django.db import models
from django.urls import reverse


class Mannequin(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    sex = models.CharField(max_length=1)
    height = models.FloatField(blank=True, null=True, default=0.0)
    neck = models.FloatField(blank=True, null=True, default=0.0)
    shoulders = models.FloatField(blank=True, null=True, default=0.0)
    bust = models.FloatField(blank=True, null=True, default=0.0)
    sleeves = models.FloatField(blank=True, null=True, default=0.0)
    waist = models.FloatField(blank=True, null=True, default=0.0)
    hips = models.FloatField(blank=True, null=True, default=0.0)
    thighs = models.FloatField(blank=True, null=True, default=0.0)
    legs = models.FloatField(blank=True, null=True, default=0.0)
    shoesize = models.FloatField(blank=True, null=True, default=0.0)
    weight = models.FloatField(blank=True, null=True, default=0.0)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(
        upload_to='mannequins', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('mannequin', kwargs={'slug': self.slug})
