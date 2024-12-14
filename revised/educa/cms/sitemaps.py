from django.contrib.sitemaps import Sitemap
from .models import Page  # Replace with the model for your CMS pages

class CMSSitemap(Sitemap):
    changefreq = "monthly"  # Indicates how often the content changes
    priority = 0.7  # Priority relative to other pages in your site

    def items(self):
        # Return all published pages in the CMS
        return Page.objects.filter(published=True)

    def location(self, obj):
        # Use the `get_absolute_url` method to generate URLs
        return obj.get_absolute_url()

    def lastmod(self, obj):
        # Return the last modified date of each page
        return obj.updated
