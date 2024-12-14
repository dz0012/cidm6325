from django.contrib.sitemaps.views import sitemap
from django.urls import path
from .sitemaps import CMSSitemap
from .feeds import CMSPageFeed
from . import views

sitemaps = {
    'cms': CMSSitemap,
}

urlpatterns = [
    path('', views.content_list, name='content_list'),
    path('upload/', views.content_upload, name='content_upload'),
    path('edit/<int:pk>/', views.content_edit, name='content_edit'),
    path('delete/<int:pk>/', views.content_delete, name='content_delete'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('feed/', CMSPageFeed(), name='cms_page_feed'),  # URL for the feed
    path('<slug:slug>/', views.page_detail, name='cms_page_detail'),  # Detail view for CMS pages
    path('export/pages/', views.export_pages_csv, name='export_pages_csv'),

]