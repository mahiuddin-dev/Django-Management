
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def get_absolute_url(self):
        return reverse("project:project_detail", args=[self.slug])

    def __str__(self):
        return self.name