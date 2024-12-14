"""
URL configuration for educa project.

The `urlpatterns` list routes URLs to views. For more information
please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include,
        path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from courses.views import CourseListView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from cms.views import export_pages_csv  # Directly import the export view
from django.contrib.sitemaps.views import sitemap
from cms.sitemaps import CMSSitemap  # Import the CMS sitemap


sitemaps = {
    'cms': CMSSitemap,
}

urlpatterns = [
    path(
        'accounts/login/', auth_views.LoginView.as_view(), name='login'
    ),
    path(
        'accounts/logout/',
        auth_views.LogoutView.as_view(),
        name='logout',
    ),
    path('admin/', admin.site.urls),
    path('course/', include('courses.urls')),
    path('', CourseListView.as_view(), name='course_list'),
    path('students/', include('students.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('api/', include('courses.api.urls', namespace='api')),
    path('chat/', include('chat.urls', namespace='chat')),
    path('cms/', include('cms.urls')),  # Include URLs from the CMS app
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )