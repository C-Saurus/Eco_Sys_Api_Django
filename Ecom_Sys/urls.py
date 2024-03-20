"""Ecom_Sys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.contrib import admin
from django.urls import path, include
from books import urls as books_urls
from clothes import urls as clothes_urls
from phones import urls as phones_urls
from user import urls as users_urls
from carts import urls as cart_urls
from search import urls as search_urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("books/", include(books_urls)),
    path("clothes/", include(clothes_urls)),
    path("phones/", include(phones_urls)),
    path("user/", include(users_urls)),
    path("search/", include(search_urls)),
    path("carts/", include(cart_urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
