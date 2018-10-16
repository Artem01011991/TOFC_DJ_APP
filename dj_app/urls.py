from django.contrib import admin
from django.urls import path, include
from .apps.main_app import urls
from .apps.rest import urls as rest_urls


urlpatterns = [
    path('', include(urls)),
    path('rest/', include(rest_urls)),
    path('admin/', admin.site.urls),
]

