from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import Page

class CMSPageFeed(Feed):
    title = "CMS Page Feed"
    link = "/cms/"  # The URL of the CMS section
    description = "Updates on new CMS pages."

    def items(self):
        # Return the latest published pages
        return Page.objects.filter(published=True).order_by('-updated')[:10]

    def item_title(self, item):
        # The title of each feed item
        return item.title

    def item_description(self, item):
        # A short description or excerpt for each feed item
        return item.content[:200]  # Truncate content to 200 characters

    def item_link(self, item):
        # The URL for each feed item
        return item.get_absolute_url()
