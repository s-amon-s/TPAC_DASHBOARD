"""TPAC_DASHBOARD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from IT_Dashboard import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^it/', include('IT_Dashboard.urls')),
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^admin/timeline/', include('admin_timeline.urls')),
]

# development mode
if settings.DEBUG:
    urlpatterns  += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns  += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)