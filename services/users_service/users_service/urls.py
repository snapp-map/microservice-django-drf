from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from .routers import router
from .views import MyTokenObtainPairView

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/token/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"
    ),  # JWT login
    path(
        "api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"
    ),  # JWT refresh
    path("api/", include(router.urls)),
]
