from django.db import models
from django.urls import reverse


# Create your models here.
class Content(models.Model):
    title = models.CharField(max_length=255, help_text="Title of the content")
    text = models.TextField(help_text="Text content", blank=True, null=True)
    file = models.FileField(upload_to='uploads/files/', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/images/', blank=True, null=True)
    video_link = models.URLField(help_text="YouTube or Vimeo video URL", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Page(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    published = models.BooleanField(default=False)  # To filter out unpublished pages
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # Generates the URL for each CMS page
        return reverse('cms_page_detail', kwargs={'slug': self.slug})