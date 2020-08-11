"""bitcoin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django.conf.urls.i18n import i18n_patterns
from bitcoin_pages import urls as pages_url
# from contact import urls as contact_url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.views.static import serve
from bitcoin_pages import views

from users import urls as users_url
from dashboard import urls as dashboard_url
from transactions import urls as transactions_url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(pages_url)),
    url(r'^transactions/', include(transactions_url)),
    url(r'^', include(users_url)),
    url(r'^', include(dashboard_url)),
    url(r'^user/', include('django.contrib.auth.urls')),
    # path('i18n/', include('django.conf.urls.i18n')),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
        )
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
        )