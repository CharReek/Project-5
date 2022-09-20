from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, 'Draft'), (1, 'Published'))


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='blog_post')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    image_url = models.URLField(max_length=1200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


class Image(models.Model):
    image_name = models.CharField(max_length=80)
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.image_name