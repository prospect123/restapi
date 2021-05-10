from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('generics.urls')),
    path('', include('mixins.urls')),
    path('', include('pagination.urls')),
    path('', include('serializations.urls')),
]