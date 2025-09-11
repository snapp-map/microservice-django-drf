from django.contrib import admin
from django.urls import path, include  # حتما include اضافه شود

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('auth.urls')),  # مسیرهای JWT
]
