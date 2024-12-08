from django.contrib import admin
from .models import Content
# Register your models here.

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'has_file', 'has_image', 'has_video_link')
    search_fields = ('title', 'text', 'video_link')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)
    fieldsets = (
        (None, {
            'fields': ('title', 'text', 'file', 'image', 'video_link')
        }),
        ('Additional Info', {
            'fields': ('created_at',),
        }),
    )

    def has_file(self, obj):
        """Check if the content has an associated file."""
        return bool(obj.file)
    has_file.boolean = True
    has_file.short_description = 'Has File'

    def has_image(self, obj):
        """Check if the content has an associated image."""
        return bool(obj.image)
    has_image.boolean = True
    has_image.short_description = 'Has Image'

    def has_video_link(self, obj):
        """Check if the content has a video link."""
        return bool(obj.video_link)
    has_video_link.boolean = True
    has_video_link.short_description = 'Has Video Link'