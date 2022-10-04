from django.db import models
from django_resized import ResizedImageField
from django.urls import reverse


# Create your models here.

class Project (models.Model):
     name = models.CharField(null=False, blank=False, max_length=15)
     image = ResizedImageField(size=[300, 220], crop=['top', 'left', 'right'], upload_to='projects')
     url = models.CharField(null=False, blank=False, max_length=255)
     github_url = models.CharField(null=False, blank=False, max_length=255)

     def __str__(self):
          return self.name

     