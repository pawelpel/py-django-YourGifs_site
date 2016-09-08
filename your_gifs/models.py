from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Category"

    def __str__(self):
        return self.name


class Post(models.Model):

    creation_date = models.DateField(auto_now=True)
    title = models.CharField(max_length=128, blank=True, null=True)
    body = models.CharField(max_length=1024, blank=True, null=True)

    author = models.ForeignKey(User)
    category = models.ForeignKey(Category)

    likes = models.IntegerField(default=0)
    url = models.CharField(max_length=256)

    video = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Posts"
        verbose_name = "Post"

    def __str__(self):
        return self.title
