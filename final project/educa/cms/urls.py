from django.urls import path
from . import views

urlpatterns = [
    path('', views.content_list, name='content_list'),
    path('upload/', views.content_upload, name='content_upload'),
    path('edit/<int:pk>/', views.content_edit, name='content_edit'),
    path('delete/<int:pk>/', views.content_delete, name='content_delete'),
]