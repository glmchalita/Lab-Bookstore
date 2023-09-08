from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'bookstore/(?P<version>(v1|v2))/', include('orderAPI.urls')),
    re_path(r'bookstore/(?P<version>(v1|v2))/', include('productAPI.urls')),
]
