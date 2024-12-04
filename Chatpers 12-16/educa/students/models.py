from django.db import models

# Create your models here.
class Upload(models.Model):
    title = models.CharField(max_length=200, help_text="Enter a title for your upload")
    text = models.TextField(blank=True, null=True, help_text="Enter some text")
    video_link = models.URLField(blank=True, null=True, help_text="Paste a video link (YouTube, Vimeo, etc.)")
    picture = models.ImageField(upload_to='pictures/', blank=True, null=True, help_text="Upload a picture")
    file = models.FileField(upload_to='files/', blank=True, null=True, help_text="Upload a file")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title