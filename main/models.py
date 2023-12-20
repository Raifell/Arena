from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify


class User(AbstractUser):
    photo = models.ImageField('Photo', upload_to='users/%Y/%m/%d', blank=True, null=True)
    slug = models.SlugField('Slug', blank=True, null=True, unique=True, max_length=255)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(User, self).save(*args, **kwargs)

