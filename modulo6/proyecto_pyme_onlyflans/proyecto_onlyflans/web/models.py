from django.db import models
from django.utils.text import slugify
import uuid


# Create your models here.

class Flan(models.Model):
    flan_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField(unique=True, blank=True)
    is_private = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Flan, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
