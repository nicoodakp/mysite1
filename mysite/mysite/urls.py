"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.conf.urls import url, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('personal.urls')),
    path('contact', include('contact.urls')),
    path('posts/', include('posts.urls')),

    path('summernote/', include('django_summernote.urls')),
    path('comments/', include('django_comments_xtd.urls')),   # url(r'^comments/', include('tow.django_ajax_comments_xtd.urls')),
    ]


if settings.DEBUG:
   urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
