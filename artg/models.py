from typing import Reversible
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.db.models.fields import related
from user.models import Profile
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    artist = models.ForeignKey('artist', on_delete=models.CASCADE)
    content = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="+")

    @property
    def children(self):
        return Comment.object.filter(parent=self).order_by('-created_on').all()

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False




class artist(models.Model):
    image = models.ImageField(upload_to='Artist', null = True)
    artist = models.CharField(max_length=100)
    description = models.TextField(null = True)
    style = models.TextField(null = True, max_length=200)
    banner = models.ImageField(upload_to='Artist', null=True)
    aimage1 = models.ImageField(upload_to='Artist', blank=True)
    atitel1 = models.TextField(blank=True)
    aimage2 = models.ImageField(upload_to='Artist', blank=True)
    atitel2 = models.TextField(blank=True)
    aimage3 = models.ImageField(upload_to='Artist', blank=True)
    atitel3 = models.TextField(blank=True)
    aimage4 = models.ImageField(upload_to='Artist', blank=True)
    atitel4 = models.TextField(blank=True)
    aimage5 = models.ImageField(upload_to='Artist', blank=True)
    atitel5 = models.TextField(blank=True)
    aimage6 = models.ImageField(upload_to='Artist', blank=True)
    atitel6 = models.TextField(blank=True)
    aimage7 = models.ImageField(upload_to='Artist', blank=True)
    atitel7 = models.TextField(blank=True)
    aimage8 = models.ImageField(upload_to='Artist', blank=True)
    atitel8 = models.TextField(blank=True)
    aimage9 = models.ImageField(upload_to='Artist', blank=True)
    atitel9 = models.TextField(blank=True)
    aimage10 = models.ImageField(upload_to='Artist', blank=True)
    atitel10 = models.TextField(blank=True)
    aimage11 = models.ImageField(upload_to='Artist', blank=True)
    atitel11 = models.TextField(blank=True)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.artist

    def get_absolute_url(self):
        return reverse('artist-detail', kwargs={'slug': self.slug})

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 200 or img.width > 200:
            output_size = (200, 200)
            img.thumbnail(output_size)
            img.save(self.image.path)
